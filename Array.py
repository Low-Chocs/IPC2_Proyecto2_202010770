from platform import node
from nodes import HeaderNode
from lists import HeaderList

class CellNode:

    def __init__(self, posX, posY, color):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.up = None
        self.down = None
        self.next = None
        self.back = None

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

class SparceMatrix:

    def __init__(self):
        self.cap = 0
        self.row = HeaderList('fila')
        self.columns = HeaderList('columns')

    def insert(self, posX, posY, color):
        newNode = CellNode(posX, posY, color)
        nodeX = self.row.getHeader(posX)
        nodeY = self.row.getHeader(posY)
        
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