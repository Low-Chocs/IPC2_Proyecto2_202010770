from re import X
from pyparsing import col
from nodes import HeaderNode
from lists import HeaderList
import webbrowser
import os

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
    
    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

class SparceMatrix:

    def __init__(self):
        self.cap = 0
        self.row = HeaderList('fila')
        self.columns = HeaderList('columns')
        self.rowSize = 0
        self.columnSize = 0
        self.resourceCounter = 0
        self.civilUnit = 0
        self.entry = 0

    def insert(self, posX, posY, color):

        if color == "gray":
            self.resourceCounter += 1
        if color == "green":
            self.entry += 1
        if color == "blue":
            self.civilUnit += 1 
            

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

    def getResourceCounter(self):
        return self.resourceCounter

    def getCivilCounter(self):
        return int(self.civilUnit)
    
    def getEntryCounter(self):
        return self.entry
    
    def getValues(self):
        return "La cantidad de entradas: {} La cantidad de recursos: {} La cantidad de unidades civiles: {}".format(self.entry, self.resourceCounter, self.civilUnit)


    def checkRow(self, row):
        header : HeaderNode = self.row.getHeader(row)
        if header == None:
            return None
            
        pointer : CellNode = header.getAccess()
        while pointer != None:
            pointer = pointer.getNext()

    
    def checkColumn(self, column):
        header : HeaderNode = self.columns.getHeader(column)
        if header == None:
            return None
        pointer : CellNode = header.getAccess()
        while pointer != None:
            pointer = pointer.getDown()
    
    def returnRowSize(self):
        return int(self.rowSize)
    
    def returnColumnSize(self):
        return int(self.columnSize)
    
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
            return None
    
    def showNode(self, row, column):
        try:
            pointer : CellNode = self.row.getHeader(row).getAccess()
            while pointer != None:
                if pointer.posX == row and pointer.posY == column:
                    return 'La pos x: {} la pos y: {} color: {}'.format(pointer.posX, pointer.posY, pointer.getColor())
                pointer = pointer.getNext()
            return None
        except:
            return None
    
    def printAll(self):

        for i in range(1,self.rowSize+1):
            for j in range(1,self.columnSize+1):
                print(self.showNode(i, j))

    def returnSelector(self, index, color, pos):
        counter=0
        for i in range(self.rowSize + 1):
            for j in range(self.columnSize + 1):
                if self.search(i, j) != None:
                    if self.search(i, j).getColor() == color:
                        counter += 1
                    if counter  == index and pos == 'x':
                        return self.search(i, j).getPosX()
                    elif counter  == index and pos == 'y':
                        return self.search(i, j).getPosY()

            

    def graphArray(self, city):
        graphArray = '''
        digraph G{
        node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
        edge[style = "invisible" dir="none"]
        node[ fillcolor="yellow" pos = "-1,1!" ]raiz;'''

        graphArray += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format(city)
        
        headerX = self.row.head
        x = 0

        while headerX != None:
            graphArray += '\n\tnode[label = "{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(headerX.id, x, headerX.id)
            headerX = headerX.next
            x += 1
        
        headerX = self.row.head
        while headerX.getNext() != None:
            graphArray += '\n\tx{}->x{}[style=invis];'.format(headerX.getId(), headerX.getNext().getId())
            graphArray += '\n\tx{}->x{}[style=invis];'.format(headerX.getId(), headerX.getNext().getId())
            headerX = headerX.getNext()
        graphArray += '\n\traiz->x{};'.format(self.row.head.getId())

        headerY = self.columns.head
        y = 0

        while headerY != None:
            graphArray += '\n\tnode[label = "{}" fillcolor="azure3" pos="{},1!" shape=box]y{};'.format(headerY.id, y, headerY.id)
            headerY = headerY.next
            y += 1
        
        headerY = self.columns.head
        while headerY.getNext() != None:
            graphArray += '\n\ty{}->y{}[style=invis];'.format(headerY.getId(), headerY.getNext().getId())
            graphArray += '\n\ty{}->y{}[style=invis];'.format(headerY.getId(), headerY.getNext().getId())
            headerY = headerY.getNext()
        graphArray += '\n\traiz->y{};'.format(self.columns.head.getId())

        header = self.row.head
        x = 0
        while header != None:
            zelda : CellNode = header.getAccess()
            while zelda != None:
                headerY = self.columns.head
                zeldaInY =0
                while headerY != None:
                    if headerY.getId() == zelda.posY: 
                        break
                    zeldaInY += 1 
                    headerY = headerY.next

                if zelda.getColor() == 'green':
                     graphArray += '\n\tnode[label="A" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                elif zelda.getColor() == 'gray':
                     graphArray += '\n\tnode[label="R" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                elif zelda.getColor() == 'blue':
                     graphArray += '\n\tnode[label="UC" fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                elif zelda.getColor() == 'white':
                     graphArray += '\n\tnode[label="*" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                elif zelda.getColor() == 'red':
                     graphArray += '\n\tnode[label="UM" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                elif zelda.getColor() == 'black':
                     graphArray += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format(zeldaInY, x, zelda.posX, zelda.posY)
                zelda = zelda.getNext()


            zelda = header.getAccess()
            while zelda.getNext() != None:
                if zelda.getNext() != None:
                    graphArray += '\n\ti{}_{}->i{}_{}[style=invisible];'.format(zelda.posX, zelda.posY,zelda.next.posX, zelda.next.posY)
                    graphArray += '\n\ti{}_{}->i{}_{}[style=invisible];'.format(zelda.posX, zelda.posY,zelda.next.posX, zelda.next.posY)
                zelda = zelda.next

            graphArray += '\n\tx{}->i{}_{}[style=invisible];'.format(header.id, header.getAccess().posX, header.getAccess().posY)
            graphArray += '\n\tx{}->i{}_{}[style=invisible];'.format(header.id, header.access.posX, header.access.posY)
            header = header.next
            x += 1

        headerY = self.columns.head
        while headerY != None:
            zeldaY : CellNode = headerY.access
            while zeldaY != None:
                if zeldaY.down != None:
                    graphArray += '\n\ti{}_{}->i{}_{}[style=invis];'.format(zeldaY.posX, zeldaY.posY,
                    zeldaY.down.posX, zeldaY.down.posY)
                    graphArray += '\n\ti{}_{}->i{}_{}[style=invis];'.format(zeldaY.posX, zeldaY.posY,
                    zeldaY.down.posX, zeldaY.down.posY) 
                zeldaY = zeldaY.down
            graphArray += '\n\ty{}->i{}_{}[style=invis];'.format(headerY.id, headerY.access.posX, headerY.access.posY)
            graphArray += '\n\ty{}->i{}_{}[style=invis];'.format(headerY.id, headerY.access.posX, headerY.access.posY)
            headerY = headerY.next

        graphArray += '\n}'

        dot = "matriz.txt".format(city)
        with open(dot, 'w') as grafo:
            grafo.write(graphArray)
        result = "matriz.pdf".format(city)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result) 

                
