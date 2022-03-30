from email import header
from nodes import CityNode
from nodes import MilitarUnitNode as MilitarNode
from nodes import RobotNode 
from nodes import HeaderNode

class CityList:

    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, city, cityArray, militarList):

        newCity=CityNode(city, cityArray, militarList)

        if self.head is None:
            self.head =newCity
            self.bottom= newCity
            self.size+=1
        else:
            pointer=self.head
            proof=True

            for i in range(self.size):
                if pointer.getCity()==city:
                    pointer.setCityArray(cityArray)
                    pointer.setMilitarList(militarList)
                    proof=False
                    break
                pointer=pointer.getNext()

            if proof:
                self.bottom.setNext(newCity)
                self.bottom= newCity
                self.size+=1
    
    def show(self):
        printer=self.head
        var=""
        for i in range(self.size):
            var+="Ciudad: {}, Matriz {}, Lista Militar: {} \n".format(printer.getCity(), 
            printer.getCityArray(), printer.getMilitarList())

            printer=printer.getNext()
        return var
    
    def showInRange(self, j):
        printer=self.head
        for i in range(self.size):
            if i==j:
                return printer.getCity()
            printer=printer.getNext()

        
    
    def len(self):
        return self.size

class MilitarList:

    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, x,y, capacity):

        newMilitarUnit=MilitarNode(x,y,capacity)
        self.size+=1

        if self.head is None:
            self.head =newMilitarUnit
            self.bottom= newMilitarUnit
        else:
            self.bottom.setNext(newMilitarUnit)
            self.bottom= newMilitarUnit

class RobotList:
    
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, type, capacity, name):

        newRobotWarrior=RobotNode(type, capacity, name)
        self.size+=1

        if self.head is None:
            self.head =newRobotWarrior
            self.bottom= newRobotWarrior
        else:
            self.bottom.setNext(newRobotWarrior)
            self.bottom= newRobotWarrior
    
    def show(self):
        printer=self.head
        var=""
        for i in range(self.size):
            if printer.getCapacity>0:
                var+="Nombre del robot: {}, de tipo {}, con la capcidad de batalla de: {} \n".format(printer.getName(), 
                printer.getType(), printer.getCapacity())
            else:
                var+="Nombre del robot: {}, de tipo {} \n".format(printer.getName(), 
                printer.getType())
            printer=printer.getNext()

        return var  

class HeaderList:

    def __init__(self, type):
        self.head=None
        self.bottom=None
        self.type=type
        self.size=0
    
    def insert(self, newNode: HeaderNode):
        self.size+=1

        if self.head == None:
            self.head=newNode
            self.bottom=newNode
        else:
            if newNode.id< self.head.id:
                newNode.next=self.head
                self.head.back=newNode
                self.head=newNode
            elif newNode.id > self.bottom.id:
                self.bottom.next=newNode
                newNode.back=self.bottom
                self.bottom=newNode
            else:
                pointer: HeaderNode =self.head
                while pointer !=None:
                    if newNode.id < pointer.id:
                        newNode.next = pointer
                        newNode.back = pointer.back
                        pointer.back.next = newNode
                        pointer.back = newNode
                        break
                    elif newNode.id > pointer.id:
                        pointer = pointer.next
                    else:
                        break
    
    def showHeader(self):
        pointer = self.head
        var=""
        
        while pointer != None:
            var+= 'Cabecera {} {} \n'.format(self.tipo, pointer.id) 
            pointer = pointer.next

    def getHeader(self, id):
        pointer = self.head

        while pointer != None:
            if id == pointer.id:
                return pointer
            pointer = pointer.next
            
            return None
