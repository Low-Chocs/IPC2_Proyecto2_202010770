class CityNode:
    def __init__(self, city, cityArray, militarList):
        self.city=city
        self.cityArray=cityArray
        self.militarList=militarList
        self.next=None
    
    def getCity(self):
        return self.city
    
    def getMilitarList(self):
        return self.militarList
    
    def getCityArray(self):
        return self.cityArray

    def setCity(self, city):
        self.city=city
    
    def setCityArray(self, cityArray):
        self.cityArray=cityArray

    
    def setMilitarList(self, militarList):
        self.militarList=militarList
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next=next
    

#This is optional
class MilitarUnitNode:

    def __init__(self, x, y, capacity):
        self.x=x
        self.y=y
        self.capacity=capacity
        self.next=None

    def getX(self):
        return self.x
    
    def getY(self):
        return self.Y
    
    def getCapacity(self):
        return self.capacity

    def setX(self, x):
        self.x=x
    
    def setY(self, y):
        self.y=y
    
    def setCapacity(self, capacity):
        self.capacity=capacity
    
    def setNext(self, next):
        self.next=next
    
    def getNext(self):
        return self.next

class RobotNode:

    def __init__(self, type, capacity, name):
        self.type=type
        self.name=name
        self.capacity=capacity
        self.next=None
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type=type

    def getCapacity(self):
        return self.capacity
    
    def setCapacity(self, capacity):
        self.capacity=capacity
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name=name

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next=next

