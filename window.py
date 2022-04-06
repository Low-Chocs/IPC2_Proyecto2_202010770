from tkinter import *
from tkinter import N, filedialog
from typing import final
from PIL import ImageTk, Image
from matplotlib.pyplot import text
from numpy import number
from Array import SparceMatrix
from lists import CityList
from lists import RobotList
from loadXml import loadXml
from lists import moveSetList

loadedFile = False
selectedCity = False
cities = CityList()
robots = RobotList()
load = loadXml(cities, robots)
city = ""
robot = ""
initialX = 0
initialY = 0
finalX = 0
finalY = 0
numberSelector = 0


def loadFile(): 
    global loadedFile                      
    route = filedialog.askopenfilename(title="Select A file", filetypes=(('xml files','*.xml'),('all files','*.*'))) 
    load.elementTree(route)
    print(robots.show())
    
    if cities.len() > 0:
        loadedFile = True

    
#CITY BUTTONS
def cityFrameOn():
    global loadedFile
    if loadedFile:
        mainFrame.pack_forget()
        cityFrame.pack(fill="both", expand="yes")
        warning.place(x=375,y=1060)
        cityBox.delete(0,END)
        for i in range(cities.len()):
            cityBox.insert(END, cities.showInRange(i))
    else:
        warning.config(text="No se ha cargado XML")
        warning.place(x=375,y=460)

def cityFrameOff():
    mainFrame.pack(fill="both", expand="yes")                                                       
    cityFrame.pack_forget()

def graphArray():
    graph = cityBox.get(ACTIVE)
    matrix : SparceMatrix = cities.returnArray(graph)
    matrix.printAll()
    matrix.graphArray(graph)

def graphSelectedArray():
    global city
    matrix : SparceMatrix = cities.returnArray(city)
    matrix.printAll()
    matrix.graphArray(city)

def selectNewCity():
    global selectedCity
    global city
    city = cityBox.get(ACTIVE)
    if city != "":
        selectedCity = True
        mainFrame.pack(fill="both", expand="yes")                                                       
        cityFrame.pack_forget()
#CITY BUTTONS END

#SELECT MISION
def operationFrameOn():
    global loadedFile
    if loadedFile and selectedCity:
        mainFrame.pack_forget()
        operationFrame.pack(fill="both", expand="yes")
        warning.place(x=375,y=1060)

    elif loadedFile and not selectedCity:
        warning.config(text="No se ha seleccionado la ciudad")
        warning.place(x=360,y=460)
    
    else: 
        warning.config(text="No se ha cargado XML ni se ha escogido ciudad")
        warning.place(x=325,y=460)


def operationFrameOff():
    mainFrame.pack(fill="both", expand="yes")                                                       
    operationFrame.pack_forget()

def rescueOperationFrameOn():
    global city
    if cities.returnArray(city).getCivilCounter() >= 1:
        operationFrame.pack_forget()
        rescueFrame.pack(fill="both", expand="yes")
        warning2.place(x=375,y=1460)
        robotRescueBox.delete(0,END)
        for i in range(robots.len()):
            robotRescueBox.insert(i, robots.returnByType(i, "ChapinRescue"))
    else:
        warning2.config(text="No hay ninguna unidad civil a rescatar")
        warning2.place(x=375,y=460)

def rescueOperationFrameOff():
    operationFrame.pack(fill="both", expand="yes")                                                       
    rescueFrame.pack_forget()

def extractionOperationFrameOn():
    global city
    if cities.returnArray(city).getResourceCounter() >= 1:
        operationFrame.pack_forget()
        extractionFrame.pack(fill="both", expand="yes")
        warning2.place(x=375,y=1060)
        robotFighterBox.delete(0,END)
        for i in range(robots.len()):
            robotFighterBox.insert(i, robots.returnByType(i, "ChapinFighter"))
    else:
        warning2.config(text="No hay ningun recurso a extraer")
        warning2.place(x=375,y=460)

def extractionOperationFrameOff():
    operationFrame.pack(fill="both", expand="yes")                                                       
    extractionFrame.pack_forget()

def extractSelection():
    global initialY
    global initialX
    global robot
    global city
    robot = ""
    global numberSelector 
    numberSelector = 0

    for i in robotFighterBox.curselection():
        robot = robots.returnSelector(i+1,"ChapinFighter").getName()
    
    if robot != "":
        
        if cities.returnArray(city).getEntryCounter() > 1:                                                    
            extractionFrame.pack_forget()
            selectEntryFrame.pack(fill="both", expand="yes")
            warning2.place(x=375,y=1060)
            selectEntryBox.delete(0,END)
            for j in range(cities.returnArray(city).returnRowSize()+1):
                for k in range(cities.returnArray(city).returnColumnSize()+1):
                    if cities.returnArray(city).search(j,k) != None:
                        if cities.returnArray(city).search(j,k).getColor() == "green":
                            selectEntryBox.insert(END, "Pos en x: {} Pos en y: {}".format(j,k))

        elif cities.returnArray(city).getEntryCounter() == 1:
            for j in range(cities.returnArray(city).returnRowSize()+1):
                for k in range(cities.returnArray(city).returnColumnSize()+1):
                    if cities.returnArray(city).search(j,k) != None:
                        if cities.returnArray(city).search(j,k).getColor() == "green":
                            initialX=j
                            initialY=k
                            print(str(j))
                            print(str(k))
            rescueSelection3()

        elif cities.returnArray(city).getEntryCounter() == 0:
            warning3.place(x=375,y=10)
            warning3.config(text="No se detecto ninguna entrada")

    

def rescueSelection():
    global initialY
    global initialX
    global robot
    global city
    robot = ""
    global numberSelector 
    numberSelector = 1

    for i in robotRescueBox.curselection():
        robot = robots.returnSelector(i+1,"ChapinRescue").getName()
    
    if robot != "":
    
        if cities.returnArray(city).getEntryCounter() > 1:                                                    
            rescueFrame.pack_forget()
            selectEntryFrame.pack(fill="both", expand="yes")
            warning2.place(x=375,y=1060)
            selectEntryBox.delete(0,END)
            for j in range(cities.returnArray(city).returnRowSize()+1):
                for k in range(cities.returnArray(city).returnColumnSize()+1):
                    if cities.returnArray(city).search(j,k) != None:
                        if cities.returnArray(city).search(j,k).getColor() == "green":
                            selectEntryBox.insert(END, "Pos en x: {} Pos en y: {}".format(j,k))
            

                    
        elif cities.returnArray(city).getEntryCounter() == 1:
            for j in range(cities.returnArray(city).returnRowSize()+1):
                for k in range(cities.returnArray(city).returnColumnSize()+1):
                    if cities.returnArray(city).search(j,k) != None:
                        if cities.returnArray(city).search(j,k).getColor() == "green":
                            initialX=j
                            initialY=k
                            print(str(j))
                            print(str(k))
            rescueSelection2()

        elif cities.returnArray(city).getEntryCounter() == 0:
            warning3.place(x=375,y=10)
            warning3.config(text="No se detecto ninguna entrada")



def rescueSelection2():
    global finalY
    global finalX
    if cities.returnArray(city).getCivilCounter() > 1:  
        selectEntryFrame.pack_forget()
        rescueFrame.pack_forget()                                                  
        selectRescueFrame.pack(fill="both", expand="yes")
        warning4.place(x=375,y=1060)
        selectEntryBox.delete(0,END)
        for j in range(cities.returnArray(city).returnRowSize()+1):
            for k in range(cities.returnArray(city).returnColumnSize()+1):
                if cities.returnArray(city).search(j,k) != None:
                    if cities.returnArray(city).search(j,k).getColor() == "blue":
                        selectRescueBox.insert(END, "Pos en x: {} Pos en y: {}".format(j,k))
    elif cities.returnArray(city).getCivilCounter() == 1:
        for j in range(cities.returnArray(city).returnRowSize()+1):
            for k in range(cities.returnArray(city).returnColumnSize()+1):
                if cities.returnArray(city).search(j,k) != None:
                    if cities.returnArray(city).search(j,k).getColor() == "blue":
                        finalX=j
                        finalY=k
                        print(str(j))
                        print(str(k))
        print("END")
    elif cities.returnArray(city).getCivilCounter() == 0:
        warning2.place(x=375,y=460)
        warning2.config(text="No se detecto ninguna unidad civil a rescatar")

def rescueSelection3():
    global finalY
    global finalX
    if cities.returnArray(city).getCivilCounter() > 1:  
        selectEntryFrame.pack_forget()
        rescueFrame.pack_forget()                                                  
        selectRescueFrame.pack(fill="both", expand="yes")
        warning4.place(x=375,y=1060)
        selectEntryBox.delete(0,END)
        for j in range(cities.returnArray(city).returnRowSize()+1):
            for k in range(cities.returnArray(city).returnColumnSize()+1):
                if cities.returnArray(city).search(j,k) != None:
                    if cities.returnArray(city).search(j,k).getColor() == "gray":
                        selectRescueBox.insert(END, "Pos en x: {} Pos en y: {}".format(j,k))
    elif cities.returnArray(city).getCivilCounter() == 1:
        for j in range(cities.returnArray(city).returnRowSize()+1):
            for k in range(cities.returnArray(city).returnColumnSize()+1):
                if cities.returnArray(city).search(j,k) != None:
                    if cities.returnArray(city).search(j,k).getColor() == "gray":
                        finalX=j
                        finalY=k
                        print(str(j))
                        print(str(k))
        print("END")
    elif cities.returnArray(city).getCivilCounter() == 0:
        warning2.place(x=375,y=460)
        warning2.config(text="No se detecto ninguna unidad civil a rescatar")

def entryBack():
    global numberSelector 
    if numberSelector == 1:
        rescueFrame.pack(fill="both", expand="yes")                                                       
        selectEntryFrame.pack_forget()
    else:
        extractionFrame.pack(fill="both", expand="yes")                                                       
        selectEntryFrame.pack_forget()


def selectEntrySpace():
    global initialX
    global initialY
    global numberSelector
    selectRescueBox.delete(0,END)

    for i in selectEntryBox.curselection():
        initialX = cities.returnArray(city).returnSelector(i+1, "green", 'x')
        initialY = cities.returnArray(city).returnSelector(i+1, "green", 'y')
        print('{},{}'.format(initialX, initialY))
    if numberSelector == 1:
        rescueSelection2()
    else:
        rescueSelection3()
    #SELECT MISION END

def selectRescueSpace():
    global initialX
    global initialY
    global finalX
    global finalY
    global numberSelector
    global robot

    for i in selectRescueBox.curselection():
        if numberSelector == 1:
            finalX = cities.returnArray(city).returnSelector(i+1, "blue", 'x')
            finalY = cities.returnArray(city).returnSelector(i+1, "blue", 'y')
            print('{},{}'.format(finalX, finalY))
            cities.returnArray(city).misionArray(initialX, initialY, finalX, finalY, robots.returnRobot(robot))
        else:
            finalX = cities.returnArray(city).returnSelector(i+1, "gray", 'x')
            finalY = cities.returnArray(city).returnSelector(i+1, "gray", 'y')
            print('{},{}'.format(finalX, finalY))
            cities.returnArray(city).misionArray(initialX, initialY, finalX, finalY, robots.returnRobot(robot))

    
    #SELECT MISION END

def selectRescueBack():
    selectRescueFrame.pack_forget()
    if cities.returnArray(city).getEntryCounter() > 1:
        selectEntryFrame.pack(fill="both", expand="yes") 
        selectEntryBox.delete(0,END)
        for j in range(cities.returnArray(city).returnRowSize()+1):
            for k in range(cities.returnArray(city).returnColumnSize()+1):
                if cities.returnArray(city).search(j,k) != None:
                    if cities.returnArray(city).search(j,k).getColor() == "green":
                        selectEntryBox.insert(END, "Pos en x: {} Pos en y: {}".format(j,k))                                                      
    else:
        rescueFrame.pack(fill="both", expand="yes")


    
    
#WINDOW
root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)
root.title("IPC2 Proyecto 2 202010770")
root.geometry("850x500")
img = ImageTk.PhotoImage(Image.open("image/sol.jpg"))
root.resizable(False, False)
#WINDOW END


#LABEL FRAMES
mainFrame=LabelFrame(root)
label=Label(mainFrame, image = img)
label.pack()
mainFrame.pack(fill="both", expand="yes")

cityFrame=LabelFrame(root)
cityFrame.pack(fill="both", expand="yes")
cityFrame.pack_forget()
img2 = ImageTk.PhotoImage(Image.open("image/paris.jpg"))
label2=Label(cityFrame, image = img2)
label2.pack()

operationFrame=LabelFrame(root)
operationFrame.pack(fill="both", expand="yes")
operationFrame.pack_forget()
label3=Label(operationFrame, image = img)
label3.pack()

extractionFrame=LabelFrame(root)
extractionFrame.pack(fill="both", expand="yes")
extractionFrame.pack_forget()
label4=Label(extractionFrame, image = img)
label4.pack()

rescueFrame=LabelFrame(root)
rescueFrame.pack(fill="both", expand="yes")
rescueFrame.pack_forget()
label4=Label(rescueFrame, image = img)
label4.pack()

selectEntryFrame = LabelFrame(root)
selectEntryFrame.pack(fill="both", expand="yes")
selectEntryFrame.pack_forget()
label4=Label(selectEntryFrame, image = img)
label4.pack()

selectRescueFrame = LabelFrame(root)
selectRescueFrame.pack(fill="both", expand="yes")
selectRescueFrame.pack_forget()
label4=Label(selectRescueFrame, image = img)
label4.pack()

selectResourceFrame = LabelFrame(root)
selectResourceFrame.pack(fill="both", expand="yes")
selectResourceFrame.pack_forget()
label4=Label(selectResourceFrame)
label4.pack()


checkEntryFrame = LabelFrame(root)
checkEntryFrame.pack(fill="both", expand="yes")
checkEntryFrame.pack_forget()
label4=Label(checkEntryFrame, image = img)
label4.pack()

checkMisionFrame = LabelFrame(root)
checkMisionFrame.pack(fill="both", expand="yes")
checkMisionFrame.pack_forget()
label4=Label(checkMisionFrame, image = img)
label4.pack()
#LABEL FRAMES END

#LABELS
warning=Label(mainFrame, text="No se han cargado el XML")
warning2=Label(operationFrame, text="No se han cargado el XML")
warning3=Label(rescueFrame, text="No se han cargado el XML")
warning4=Label(extractionFrame, text="No se han cargado el XML")
#LABELS END

#ListBox
cityBox = Listbox(cityFrame, height=18, width=110)
cityBox.place(x=130, y=75)


robotFighterBox = Listbox(extractionFrame, height=18, width=110)
robotFighterBox.place(x=130, y=75)

robotRescueBox = Listbox(rescueFrame, height=18, width=110)
robotRescueBox.place(x=130, y=75)

selectEntryBox = Listbox(selectEntryFrame, height=18, width=110)
selectEntryBox.place(x=130, y=75)

selectRescueBox = Listbox(selectRescueFrame, height=18, width=110)
selectRescueBox.place(x=130, y=75)

#LIST BOX END


#BUTTONS 
selectFileButton = Button(mainFrame, text="Seleccionar Archivo XML", width=25, height=5, command=loadFile)
selectFileButton.pack()
selectFileButton.place(x=355, y=100)

selectCity = Button(mainFrame, text="Seleccioniar Ciudad", width=25, height=5, command=cityFrameOn)
selectCity.pack()
selectCity.place(x=355, y=200)

selectCityBack = Button(cityFrame, text="Regresar", width=15, height=3, command=cityFrameOff)
selectCityBack.pack()
selectCityBack.place(x=10, y=10)

showGraphBotton= Button(cityFrame, text="Graficar Ciudad", width=25, height=3, command=graphArray)
showGraphBotton.pack()
showGraphBotton.place(x=235, y=400)

selectCityBotton= Button(cityFrame, text="Seleccionar Ciudad", width=25, height=3, command=selectNewCity)
selectCityBotton.pack()
selectCityBotton.place(x=505, y=400)

operations = Button(mainFrame, text="Operaciones", width=25, height=5, command=operationFrameOn)
operations.pack()
operations.place(x=355, y=300)

operationsRescue = Button(operationFrame, text="Rescate", width=25, height=5, command=rescueOperationFrameOn)
operationsRescue.pack()
operationsRescue.place(x=455, y=200)

operationsRescueBack = Button(rescueFrame, text="Regresar", width=15, height=3, command=rescueOperationFrameOff)
operationsRescueBack.pack()
operationsRescueBack.place(x=10, y=10)

operationsFight = Button(operationFrame, text="Extración", width=25, height=5, command=extractionOperationFrameOn)
operationsFight.pack()
operationsFight.place(x=255, y=200)

selectExtractRobot = Button(extractionFrame, text="Seleccione robot de extracción", width=25, height=5, command=extractSelection)
selectExtractRobot.pack()
selectExtractRobot.place(x= 365, y=410)

selectRescueRobot = Button(rescueFrame, text="Seleccione robot de rescate", width=25, height=5, command=rescueSelection)
selectRescueRobot.pack()
selectRescueRobot.place(x= 365, y=410)

operationsExtractionBack = Button(extractionFrame, text="Regresar", width=15, height=3, command=extractionOperationFrameOff)
operationsExtractionBack.pack()
operationsExtractionBack.place(x=10, y=10)

operationBack = Button(operationFrame, text="Regresar", width=15, height=3, command=operationFrameOff)
operationBack.pack()
operationBack.place(x=10, y=10)

selectEntryBack = Button(selectEntryFrame, text="Regresar", width=15, height=3, command=entryBack)
selectEntryBack.pack()
selectEntryBack.place(x=10, y=10)

selectRescueBackButton = Button(selectRescueFrame, text="Regresar", width=15, height=3, command=selectRescueBack)
selectRescueBackButton.pack()
selectRescueBackButton.place(x=10, y=10)

checkEntryCity = Button(selectEntryFrame, text="Ver ciudad", width=15, height=3, command=graphSelectedArray)
checkEntryCity.pack()
checkEntryCity.place(x= 265, y=410)


selectEntryCity = Button(selectEntryFrame, text="Seleccionar entrada", width=15, height=3, command=selectEntrySpace)
selectEntryCity.pack()
selectEntryCity.place(x= 465, y=410)

checkRescueCity = Button(selectRescueFrame, text="Ver ciudad", width=15, height=3, command=graphSelectedArray)
checkRescueCity.pack()
checkRescueCity.place(x= 265, y=410)

selectRescueCityButton = Button(selectRescueFrame, text="Graficar", width=15, height=3, command=selectRescueSpace)
selectRescueCityButton.pack()
selectRescueCityButton.place(x= 465, y=410)

#BUTTONS END

#Loop
root.mainloop()