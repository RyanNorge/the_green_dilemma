class Node:
    def __init__(self, xPos, yPos, Alive):
        self.xPos=xPos
        self.yPos=yPos
        self.isAlive=Alive

        self.topNeighbor
        self.bottomNeighbor
        self.leftNeighbor
        self.rightNeighbor

    def createRightNeighbor(self, xSize, ySize):
        self.rightNeigbor=Node(self.xPos+1, yPos, not Alive)
        if ySize>0:
            self.rightNeighbor.createRightNeighbor(xSize, ySize-1)

        self.rightNeighbor.createBottomNeighbor(xSize-1)

    def createBottomNeighbor(self, xSize):
        self.bottomNeighbor=Node(self.xPos, self.yPos-1, not Alive)
        self.bottomNeighbor.createBottomNeighbor(xSize-1)

        



    

