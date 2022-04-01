from tkinter import *
from tkinter import N, filedialog
from PIL import ImageTk, Image
from Array import SparceMatrix
from lists import CityList
from lists import RobotList
from loadXml import loadXml

loadedFile=False
cities=CityList()
robots=RobotList()
load=loadXml(cities, robots)


def loadFile(): 
    global loadedFile                 
                                  
    route = filedialog.askopenfilename(title="Select A file", filetypes=(('xml files','*.xml'),('all files','*.*'))) 
    load.elementTree(route)
    if cities.len() >0:
        loadedFile=True
    

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
        warning.place(x=375,y=460)

def cityFrameOff():
    mainFrame.pack(fill="both", expand="yes")                                                       
    cityFrame.pack_forget()

def graphArray():
    graph = cityBox.get(ACTIVE)
    matrix : SparceMatrix = cities.returnArray(graph)
    matrix.printAll()
    matrix.graphArray(graph)
    
#Window
root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)
root.title("IPC2 Proyecto 2 202010770")
root.geometry("850x500")
img = ImageTk.PhotoImage(Image.open("image/sol.jpg"))

#Label frames
mainFrame=LabelFrame(root)
label=Label(mainFrame, image = img)
label.pack()
mainFrame.pack(fill="both", expand="yes")

cityFrame=LabelFrame(root)
label=Label(cityFrame, image = img)
label.pack()
cityFrame.pack(fill="both", expand="yes")
cityFrame.pack_forget()

#Labels
warning=Label(mainFrame, text="No se han cargado el XML")

#ListBox
cityBox = Listbox(cityFrame, height=18, width=110)
cityBox.place(x=130, y=75)


#Buttons
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

selectCityBotton= Button(cityFrame, text="Seleccionar Ciudad", width=25, height=3, command=cityFrameOn)
selectCityBotton.pack()
selectCityBotton.place(x=505, y=400)

operations = Button(mainFrame, text="Operaciones", width=25, height=5, command=cityFrameOff)
operations.pack()
operations.place(x=355, y=300)

#Loop
root.mainloop()