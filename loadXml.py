from tkinter import N, filedialog
from xml.etree import ElementTree as et
from lists import CityList
from lists import RobotList
from Array import SparceMatrix

class loadXml:

    def __init__(self, cityList: CityList, robotList: RobotList):
        self.cityList=cityList
        self.robotList =robotList
        self.array = SparceMatrix()

    def elementTree(self, ruta):
        tree = et.parse(ruta)
        root = tree.getroot()
        row=0

        for element in root:

            if element.tag=='listaCiudades':
                
                for subelement in element:
                    row=0
                    for subelement2 in subelement:

                        if subelement2.tag == 'nombre':
                            cityName = subelement2.text
                        elif subelement2.tag == 'fila':
                            row+=1
                            column=0
                            for char in subelement2.text:
                                if char != "\"":
                                    column+=1
                                    if char == 'E':
                                        self.array.insert(row, column, "green")
                                    if char == 'R':
                                        self.array.insert(row, column, "gray")
                                    elif char == 'C':
                                        self.array.insert(row, column, "blue")
                                    elif char == ' ':
                                        self.array.insert(row, column, "white")

                        elif subelement2.tag == 'unidadMilitar':
                            militaryRow = subelement2.attrib['fila']
                            militaryColumn = subelement2.attrib['columna']
                            militaryCapacity = subelement2.text
                            if self.array.search(int(militaryRow), int(militaryColumn)) != None:
                                self.array.search(int(militaryRow), int(militaryColumn)).setColor('red')
                                self.array.search(int(militaryRow), int(militaryColumn)).setCapacity(int(militaryCapacity))
                            else:
                                self.array.insert(int(militaryRow), int(militaryColumn), "red")

                    self.cityList.insert(cityName, self.array)
                    self.array = SparceMatrix()


            elif element.tag == 'robots':

                for subelement in element:
                    for subelement2 in subelement:
                        robotName=subelement2.text
                        robotType = subelement2.attrib['tipo']
                        
                        if robotType == "ChapinRescue":
                            robotCapacity=0
                        else:
                            robotCapacity = int(subelement2.attrib['capacidad'])
                        self.robotList.insert(robotType, int(robotCapacity), robotName)

    def showCity(self):
        self.cityList.show()





