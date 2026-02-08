import random


class Node:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None

        self.nextAlive = False
        self.isAlive = random.choice([True, False])
        self.fertilized=False
        self.fertilizerCountDown=0

    def changeAliveStatus(self, alive):
        self.isAlive = alive

    def checkNextUpdate(self):
        aliveNeighbors = 0
        if self.top and self.top.isAlive:
            aliveNeighbors += 1
        if self.bottom and self.bottom.isAlive:
            aliveNeighbors += 1
        if self.left and self.left.isAlive:
            aliveNeighbors += 1
        if self.right and self.right.isAlive:
            aliveNeighbors += 1
        if self.top_left and self.top_left.isAlive:
            aliveNeighbors += 1
        if self.top_right and self.top_right.isAlive:
            aliveNeighbors += 1
        if self.bottom_left and self.bottom_left.isAlive:
            aliveNeighbors += 1
        if self.bottom_right and self.bottom_right.isAlive:
            aliveNeighbors += 1

        if self.isAlive:
            if aliveNeighbors == 2 or aliveNeighbors == 3:
                self.nextAlive = True
            else:
                self.nextAlive = False

        else:
            if aliveNeighbors == 3:
                self.nextAlive = True
            else:
                self.nextAlive = False

    def updateStatus(self):
        self.isAlive = self.nextAlive


def build_grid(width, height):

    # Create nodes
    grid = []
    for x in range(width):
        grid.append([])
        for y in range(height):
            grid[x].append(Node(x, y))

    # Helper to get node or None
    def get(x, y):
        if 0 <= x < width and 0 <= y < height:
            return grid[y][x]
        return None

    # Link neighbors
    for y in range(height):
        for x in range(width):
            node = grid[y][x]
            node.top = get(x, y - 1)
            node.bottom = get(x, y + 1)
            node.left = get(x - 1, y)
            node.right = get(x + 1, y)
            node.top_left = get(x - 1, y - 1)
            node.top_right = get(x + 1, y - 1)
            node.bottom_left = get(x - 1, y + 1)
            node.bottom_right = get(x + 1, y + 1)
    return grid


# Method for calling checkNextUpdate on all nodes in the grid
def checkNextUpdateAll(grid):
    for x in grid:
        for y in grid[x]:
            grid[x][y].checkNextUpdate()


# Method for calling updateStatus on all nodes in the grid
def updateStatusAll(grid):
    for x in grid:
        for y in grid[x]:
            grid[x][y].updateStatus()


def updateAllNodes(grid):
    checkNextUpdateAll(grid)
    updateStatusAll(grid)


# finner den nærmeste noden som lever
def shortestAlive(Graph, start):
    visited = {start}
    queue = []

    # Add all 8 neighbors of start to queue
    for neighbor in [
        start.top_left,
        start.left,
        start.bottom_left,
        start.bottom,
        start.bottom_right,
        start.right,
        start.top_right,
        start.top,
    ]:
        queue.append(neighbor)
        visited.add(neighbor)

    while queue:
        n = queue.pop(0)

        # Check all 8 neighbors
        for neighbor in [
            n.top_left,
            n.left,
            n.bottom_left,
            n.bottom,
            n.bottom_right,
            n.right,
            n.top_right,
            n.top,
        ]:
            if neighbor is None:
                continue
            if neighbor.isAlive:
                return neighbor
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return None


# Funksjon for å finne retningen til et koordinat
#returnerer en liste med koordinater på formen [x,y]
def findDirection(Graph, start):
    targetNode = shortestAlive(Graph, start)
    targetX = targetNode.xPos
    targetY = targetNode.yPos
    startX=start.xPos
    startY=start.yPos

    if (abs(targetX-startX)>abs(targetY-startY)):
        if targetX>startX:
            return [startX+1, startY]

        else:
            return [startX-1, startY]
    
    else:
        if targetY>startY:
            return [startX, startY+1]
        else:
            return [startX, startX-1]

