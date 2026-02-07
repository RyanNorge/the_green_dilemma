class Node:
    def __init__(self, xPos, yPos, xSize, ySize, Alive):
        self.xPos=xPos
        self.yPos=yPos
        self.xSize=xSize
        self.ySize=ySize
        self.isAlive=Alive

        self.topNeighbor
        self.bottomNeighbor
        self.leftNeighbor
        self.rightNeighbor
        self.leftTopNeighbor
        self.leftBottomNeighbor
        self.rightTopNeighbor
        self.rightBottomNeighbor

    def createRightNeighbor(self,leftNeighbor):
        self.rightNeighbor=Node(self.xPos+1, self.yPos, self.xSize, self.ySize, not self.Alive)
        self.rightNeighbor.leftNeighbor=leftNeighbor

        if self.xSize-self.xPos<=0: #Recursively creates nodes on X axis
            self.rightNeighbor.createRightNeighbor(self)

        self.rightNeighbor.createBottomNeighbor(self.leftNeighbor, self.rightNeighbor, self)


    def createBottomNeighbor(self, leftNeighbor, rightNeighbor, topNeighbor):
        self.bottomNeighbor=Node(self.xPos, self.yPos-1, not self.Alive)

        self.bottomNeighbor.leftNeighbor=leftNeighbor
        self.bottomNeighbor.rightNeighbor=rightNeighbor
        self.bottomNeighbor.topNeighbor=topNeighbor

        if self.ySize-self.yPos <=0: #Recursively creates nodes on Y axis
            self.bottomNeighbor.createBottomNeighbor(self.leftNieghbor.bottomNeighbor, self.rightNeighbor.bottomNeighbor, self)

        



    

