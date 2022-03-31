from tkinter import *
from tkinter import N, filedialog
from PIL import ImageTk, Image
import os
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
    load.showCity()
    

def cityFrameOn():
    global loadedFile
    if loadedFile:
        mainFrame.pack_forget()
        cityFrame.pack(fill="both", expand="yes")
        warning.place(x=375,y=1060)
        for i in range(list.len()):
            cityBox.insert(END, list.showInRange(i))
    else:
        warning.place(x=375,y=460)

def cityFrameOff():
    mainFrame.pack(fill="both", expand="yes")                                                       
    cityFrame.pack_forget()




#We create the window
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


#Here comes the buttons
selectFileButton = Button(mainFrame, text="Seleccionar Archivo XML", width=25, height=5, command=loadFile)
selectFileButton.pack()
selectFileButton.place(x=355, y=100)

selectCity = Button(mainFrame, text="Seleccioniar Ciudad", width=25, height=5, command=cityFrameOn)
selectCity.pack()
selectCity.place(x=355, y=200)

selectCityBack = Button(cityFrame, text="Regresar", width=15, height=3, command=cityFrameOff)
selectCityBack.pack()
selectCityBack.place(x=10, y=10)

showGraphBotton= Button(cityFrame, text="Mostrar Ciudad", width=25, height=3, command=cityFrameOn)
showGraphBotton.pack()
showGraphBotton.place(x=235, y=400)

selectCityBotton= Button(cityFrame, text="Seleccionar Ciudad", width=25, height=3, command=cityFrameOn)
selectCityBotton.pack()
selectCityBotton.place(x=505, y=400)

operations = Button(mainFrame, text="Operaciones", width=25, height=5, command=cityFrameOff)
operations.pack()
operations.place(x=355, y=300)

root.mainloop()