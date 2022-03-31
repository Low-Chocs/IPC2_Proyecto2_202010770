from pyparsing import col
from nodes import HeaderNode
from lists import HeaderList

class CellNode:

    def __init__(self, posX, posY, color):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.capacity=0
        self.up = None
        self.down = None
        self.next = None
        self.back = None
    
    def setCapacity(self, capacity):
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def setUp(self, up):
        self.up = up

    def getUp(self):
        return self.up
   
    def getDown(self):
        return self.down
    
    def setDown(self, down):
        self.down = down
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

    def getBack(self):
        return self.back
    
    def setBack(self, back):
        self.back = back
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

class SparceMatrix:

    def __init__(self):
        self.cap = 0
        self.row = HeaderList('fila')
        self.columns = HeaderList('columns')
        self.rowSize=0
        self.columnSize=0

    def insert(self, posX, posY, color):
        newNode = CellNode(posX, posY, color)
        nodeX = self.row.getHeader(posX)
        nodeY = self.columns.getHeader(posY)

        if posX>self.rowSize:
            self.rowSize=posX

        if posY>self.columnSize:
            self.columnSize=posY
        
        if nodeX == None:
            nodeX = HeaderNode(posX)
            self.row.insert(nodeX)
        
        if nodeY == None:
            nodeY = HeaderNode(posY)
            self.columns.insert(nodeY)
        
        if nodeX.getAccess()== None:
            nodeX.setAccess(newNode)

        else:
            
            if newNode.posX < nodeX.getAccess().posY:
                newNode.setNext(nodeX.getAccess())
                nodeX.getAccess().setBack(newNode)
                nodeX.setAccess(newNode)
            else:

                if newNode.posY < nodeX.getAccess().posY:
                    newNode.setNext(nodeX.getAccess())
                    nodeX.getAccess().setBack(newNode)
                    nodeX.setAccess(newNode)
                else:
                    pointer: CellNode = nodeX.getAccess()

                    while pointer != None:
                        if newNode.posY < pointer.posY:
                            newNode.setNext(pointer)
                            newNode.setBack(pointer.getBack())
                            pointer.getBack().setNext(newNode)
                            pointer.setBack(newNode)
                            break
                        elif newNode.posX == pointer.posX and newNode.posY == pointer.posY:
                            break
                        else:
                            if pointer.getNext() == None:
                                pointer.setNext(newNode)
                                newNode.setBack(pointer)
                                break
                            else:
                                pointer = pointer.getNext()
        
        if nodeY.getAccess() == None:
            nodeY.setAccess(newNode)
        else:
            if newNode.posX < nodeY.getAccess().posX:
                newNode.setDown(nodeY.getAccess())
                nodeY.getAccess().setUp(newNode)
                nodeY.setAccess(newNode)
            else:
                pointer2 : CellNode = nodeY.getAccess()

                while pointer2 != None:
                    if newNode.posX < pointer2.posX:
                        newNode.setDown(pointer2)
                        newNode.setUp(pointer2.getUp())
                        pointer2.getUp().setDown(newNode)
                        pointer2.setUp(newNode)
                        break
                    elif newNode.posX == pointer2.posX and newNode.posY == pointer2.posY:
                        break
                    else:
                        if pointer2.getDown() == None:
                            pointer2.setDown(newNode)
                            newNode.setUp(pointer2)
                            break
                        else:
                            pointer2 = pointer2.getDown()

    def checkRow(self, row):
        header : HeaderNode = self.row.getHeader(row)
        if header == None:
            print('Esa coordenada de row no existe')
            return None
            
        pointer : CellNode = header.getAccess()
        while pointer != None:
            print(pointer.color)
            pointer = pointer.getNext()

    
    def checkColumn(self, column):
        header : HeaderNode = self.columns.getHeader(column)
        if header == None:
            print('Esa coordenada de columna no existe')
            return None

        pointer : CellNode = header.getAccess()
        while pointer != None:
            print(pointer.color)
            pointer = pointer.getDown()
    
    def rowSize(self):
        return self.rowSize
    
    def columnSize(self):
        return self.columnSize
    
    def editRow(self):
        self.rowSize=0
    
    def editColumn(self):
        self.ColumnSize=0

    def search(self, row, column):
        try:
            pointer : CellNode = self.row.getHeader(row).getAccess()
            while pointer != None:
                if pointer.posX == row and pointer.posY == column:
                    return pointer
                pointer = pointer.getNext()
            return None
        except:
            print('Coordenada no encontrada')
            return None
    
    def showNode(self, row, column):
        try:
            pointer : CellNode = self.row.getHeader(row).getAccess()
            while pointer != None:
                if pointer.posX == row and pointer.posY == column:
                    return 'La pos x: {} la pos y: {} color: {}'.format(pointer.posX, pointer.posY, pointer.getColor())
                pointer = pointer.getNext()
            return
        except:
            print('Coordenada no encontrada')
            return
    
    def printAll(self):

        for i in range(1,self.rowSize+1):
            for j in range(1,self.columnSize+1):
                print(self.showNode(i, j))


array = SparceMatrix()
array.insert(6,5,"ORAL")
array.insert(4,2,"AMIGO")
array.insert(1,2,"NEGRO")
array.insert(1,3,"NEGRO22222")
array.insert(1,1,"BLANCO")
array.insert(5,1,"NEGRO2222")
array.insert(5,8,"NEGRO2222")
array.insert(6,3,"ORIGINAL")
 

