from types import NoneType
from nodes import CityNode
from nodes import RobotNode 
from nodes import HeaderNode

class CityList:

    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, city, cityArray):

        newCity=CityNode(city, cityArray)
        proof =True

        if self.head is None:
            self.head = newCity
            self.bottom = newCity
            self.head.setNext(self.bottom)
            self.head.setBack(self.head)
            self.size+=1
        else:
            pointer = self.head
            for i in range(self.size):
                if pointer.getCity()==city:
                    pointer.setCityArray(cityArray)
                    proof=False
                    break
                pointer=pointer.getNext()

            if proof:
                pointer2 = self.head

                for i in range(self.size):
                    if self.size >= 2:
                        if city > self.head.getCity():
                            if city > self.bottom.getCity():
                                print("Numero " ,str(i))
                                self.bottom.setNext(newCity)
                                newCity.setBack(self.bottom)
                                self.bottom = newCity
                                print(self.bottom.getBack())
                                self.size += 1
                                break
                            elif city > pointer2.getCity():
                                pointer2 = pointer2.getNext()
                                continue
                            elif city < pointer2.getCity():
                                newCity.setNext(pointer2)
                                pointer2.getBack().setNext(newCity)
                                newCity.setBack(pointer2.getBack())
                                pointer2.setBack(newCity)
                                self.size +=1
                                break
                        else:
                            newCity.setNext(self.head)
                            newCity.getNext().setBack(newCity)
                            self.head = newCity
                            self.size +=1
                            break

                    else:
                        if city > self.head.getCity():
                            self.head.setNext(newCity)
                            self.bottom.setBack(self.head)
                            self.bottom = newCity
                            self.size+=1
                            break
                        else:
                            newCity.setNext(self.bottom)
                            self.bottom.setBack(newCity)
                            self.head = newCity
                            self.size+=1
                            break


        
    def returnArray(self, city):
        pointer = self.head
        counter = 0

        while pointer != None:
            if pointer.getCity() == city:
                    return pointer.getCityArray()
            pointer = pointer.getNext()

    
    def show(self):
        pointer: CityNode=self.head
        var=""
        for i in range(self.size):
            disperseArray = pointer.getCityArray()
            disperseArray.printAll()
            pointer = pointer.next
        return var
    
    def showCity(self):
        pointer: CityNode=self.head
        var=""
        counter = 0
        for i in range(self.size):
            print(pointer)
            counter +=1
            var += "Esta es una ciudad "+pointer.getCity()
            pointer = pointer.next
        return var

    def showInRange(self, j):
        printer=self.head
        for i in range(self.size):
            if i==j and printer != NoneType:
                return printer.getCity()
            printer=printer.getNext()

    def showInverse(self):
        printer = self.bottom

        for i in range(self.size):
            print(printer.getCity())
            printer = printer.getBack()


    def len(self):
        return self.size

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
            if printer.getCapacity()>0:
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
                while pointer != None:
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

