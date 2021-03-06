class CityNode:
    def __init__(self, city, cityArray):
        self.city = city
        self.cityArray = cityArray
        self.next = None
        self.back = None
    
    def getCity(self):
        return self.city
    
    def getCityArray(self):
        return self.cityArray

    def setCity(self, city):
        self.city=city
    
    def setCityArray(self, cityArray):
        self.cityArray=cityArray
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next=next
    
    def getBack(self):
        return self.back
    
    def setBack(self, back):
        self.back = back

class RobotNode:

    def __init__(self, type, capacity, name):
        self.type=type
        self.name=name
        self.capacity=capacity
        self.next=None
        self.back = None
    
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

    def getBack(self):
        return self.back
    
    def setBack(self, back):
        self.back = back

class HeaderNode():
    def __init__(self, id):
        self.id=id
        self.next=None
        self.back=None
        self.access=None
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next=next

    def getBack(self):
        return self.back
    
    def setBack(self, back):
        self.back=back
    
    def getAccess(self):
        return self.access
    
    def setAccess(self, access):
        self.access=access

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id=id
    
class moveSetNode:

    def __init__(self, posX, posY, options, direction):
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.options = options
        self.next = None
        self.back = None
        self.satus = True

    def getStatus(self):
        return self.status

    def setStatus(self):
        self.status = False

    def getNext(self):
        return self.next
    
    def getDirection(self):
        return self.direction
    
    def setNext(self, next):
        self.next=next

    def getBack(self):
        return self.back
    
    def setBack(self, back):
        self.back=back

    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getOptions(self):
        return self.options
    
    def setOptions(self, options):
        self.options = options




