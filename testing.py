from tkinter import N, filedialog
from xml.etree import ElementTree as et



def elementTree(ruta):
    tree = et.parse(ruta)
    root = tree.getroot()

    for element in root:

        if element.tag=='listaCiudades':
            
            for subelement in element:

                for subelement2 in subelement:

                    if subelement2.tag == 'nombre':
                        cityName = subelement2.text
                    elif subelement2.tag == 'fila':
                        cityRow = subelement2.text
                    elif subelement2.tag == 'unidadMilitar':
                        militaryBase = subelement2.text

                print(cityName, cityRow, militaryBase)

        elif element.tag == 'robots':

            for subelement in element:
                for subelement2 in subelement:
                    robotName=subelement2.text
                    robotType = subelement2.attrib['tipo']
                    
                    if robotType == "ChapinRescue":
                        robotCapacity=0
                    else:
                        robotCapacity = subelement2.attrib['capacidad']
                    
                    print(robotName,robotType,robotCapacity)

route = filedialog.askopenfilename(title="Select A file", filetypes=(('xml files','*.xml'),('all files','*.*')))  
elementTree(route)

