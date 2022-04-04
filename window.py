from tkinter import *
from tkinter import N, filedialog
from PIL import ImageTk, Image
from matplotlib.pyplot import text
from Array import SparceMatrix
from lists import CityList
from lists import RobotList
from loadXml import loadXml

loadedFile = False
selectedCity = False
cities = CityList()
robots = RobotList()
load = loadXml(cities, robots)
city = ""
robot = ""


def loadFile(): 
    global loadedFile                      
    route = filedialog.askopenfilename(title="Select A file", filetypes=(('xml files','*.xml'),('all files','*.*'))) 
    load.elementTree(route)
    print(robots.show())
    
    if cities.len() > 0:
        loadedFile = True

    

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

def selectNewCity():
    global selectedCity
    global city
    city = cityBox.get(ACTIVE)
    if city != "":
        selectedCity = True
        mainFrame.pack(fill="both", expand="yes")                                                       
        cityFrame.pack_forget()


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
    for i in robotFighterBox.curselection():
        print(robots.returnSelector(i+1,"ChapinFighter").getName())

def rescueSelection():
    global robot
    global city
    robot = ""

    for i in robotRescueBox.curselection():
        robot = robots.returnSelector(i+1,"ChapinRescue").getName()

    if robot != "":
        print("Yayui"+str(cities.returnArray(city).getEntryCounter()))

        if cities.returnArray(city).getEntryCounter() > 1:                                                    
            rescueFrame.pack_forget()
            selectEntryFrame.pack(fill="both", expand="yes")
            warning2.place(x=375,y=1060)

        elif cities.returnArray(city).getEntryCounter() == 1:
            
            if cities.returnArray(city).getCivilCounter() > 1:                                                    
                rescueFrame.pack_forget()
                selectRescueFrame.pack(fill="both", expand="yes")
                warning4.place(x=375,y=1060)
            elif cities.returnArray(city).getCivilCounter() == 1:
                print("Pase")
            elif cities.returnArray(city).getCivilCounter() == 0:
                warning2.place(x=375,y=460)
                warning2.config(text="No se detecto ninguna unidad civil a rescatar")

        elif cities.returnArray(city).getEntryCounter() == 0:
            warning3.place(x=375,y=10)
            warning3.config(text="No se detecto ninguna entrada")

    
    
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
#BUTTONS END

#Loop
root.mainloop()