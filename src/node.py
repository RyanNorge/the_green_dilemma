import random


class Node:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.nextAlive = False
        self.isAlive = random.choice([True, False])
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None

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
    for row in grid:
        for node in row:
            node: Node
            node.checkNextUpdate()


# Method for calling updateStatus on all nodes in the grid
def updateStatusAll(grid):
    for row in grid:
        for node in row:
            node: Node
            node.updateStatus()


def updateAllNodes(grid):
    checkNextUpdateAll(grid)
    updateStatusAll(grid)
