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
        self.fertilized = False
        self.fertilizerCountDown = 0

    def changeAliveStatus(self, alive):
        self.isAlive = alive

    def checkNextUpdate(self):
        aliveNeighbors = 0
        for neighbor in [
            self.top,
            self.bottom,
            self.top_left,
            self.top_right,
            self.bottom_left,
            self.bottom_right,
            self.right,
            self.left,
        ]:
            if neighbor and neighbor.isAlive:
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
        if self.nextAlive == False:
            if self.fertilizerCountDown < 1:
                self.isFertilized = False
                self.fertilizerCountDown = 0
                self.isAlive = False

        if self.nextAlive == False:
            if self.fertilizerCountDown < 1:
                self.isFertilized = False
                self.fertilizerCountDown = 0
                self.isAlive = False

            else:
                self.fertilizerCountDown -= 1

                self.fertilizerCountDown -= 1

        else:
            self.isAlive = True
            self.isAlive = True

    def fertilize(self):
        self.isFertilized = True
        self.fertilizerCountDown = 5


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


# finner den nærmeste noden som lever
def shortestAlive(Graph, start) -> Node | None:
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
        if neighbor:
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
#  returnerer en liste med koordinater på formen [x,y]
def findDirection(Graph, startX, startY) -> list[int, int]:
    startNode = Graph[startX][startY]
    print(startNode)
    targetNode = shortestAlive(Graph, startNode)

    if targetNode is None:
        return [startX, startY]

    targetX = targetNode.xPos
    targetY = targetNode.yPos

    if abs(targetX - startX) > abs(targetY - startY):
        if targetX > startX:
            return [startX + 1, startY]
        else:
            return [startX - 1, startY]

    elif abs(targetX - startX) < abs(targetY - startY):
        if targetY > startY:
            return [startX, startY + 1]
        else:
            return [startX, startY - 1]

    return [startX, startY]
