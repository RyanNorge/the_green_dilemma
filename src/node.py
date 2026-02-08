import random
import copy

import pygame

DIRT_TILE = pygame.image.load("assets/DirtTile.png")
FLOWER_TILE = pygame.image.load("assets/FlowerTile.png")
GRASS_TILE = pygame.image.load("assets/GrassTile.png")

UNSPROUTED_TILE = pygame.image.load("assets/UnsproutedTile.png")

GROWING_TILES = (DIRT_TILE, UNSPROUTED_TILE, GRASS_TILE)
DYING_TILES = (GRASS_TILE, DIRT_TILE)


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
        self.wasAlive = copy.copy(self.isAlive)
        self.fertilized = False
        self.fertilizerCountDown = 0

        self.sprites_set = []
        self.sprites_set.append(GRASS_TILE if self.isAlive else DIRT_TILE)
        self.sprite_frame = 0

    def changeAliveStatus(self, alive):
        self.isAlive = alive
        self.sprites_set = DYING_TILES
        self.sprite_frame = 99

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
        if not self.nextAlive:
            if self.fertilizerCountDown < 1:
                self.isFertilized = False
                self.fertilizerCountDown = 0
                self.isAlive = False

            else:
                self.fertilizerCountDown -= 1

        else:
            self.isAlive = True

    def updateSprite(self):

        self.sprite_frame += 1

        if self.isAlive and not self.wasAlive:
            self.sprites_set = GROWING_TILES
            self.sprite_frame = 0

        if not self.isAlive and self.wasAlive:
            self.sprites_set = DYING_TILES
            self.sprite_frame = 0

        self.wasAlive = self.isAlive

    def getSprite(self) -> pygame.Surface:
        index = min(self.sprite_frame, len(self.sprites_set) - 1)
        return self.sprites_set[index]

    def fertilize(self):
        self.isFertilized = True
        self.fertilizerCountDown = 5


def build_grid(width, height):

    # Create nodes
    grid = []
    # grid is indexed as grid[x][y] (x = column, y = row)
    for x in range(width):
        grid.append([])
        for y in range(height):
            grid[x].append(Node(x, y))

    # Helper to get node or None
    def get(x, y):
        # return node at column x and row y, or None if out of bounds
        if 0 <= x < width and 0 <= y < height:
            return grid[x][y]
        return None

    # Link neighbors (iterate columns then rows to match grid[x][y])
    for x in range(width):
        for y in range(height):
            node = grid[x][y]
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
    # Breadth-first search from start to find the nearest alive node
    if start is None:
        return None

    visited = set()
    queue = []

    visited.add(start)

    # seed queue with start's neighbors
    for n in [
        start.top_left,
        start.top,
        start.top_right,
        start.left,
        start.right,
        start.bottom_left,
        start.bottom,
        start.bottom_right,
    ]:
        if n is not None:
            queue.append(n)
            visited.add(n)

    while queue:
        n = queue.pop(0)
        if n.isAlive:
            return n

        for nbr in [
            n.top_left,
            n.top,
            n.top_right,
            n.left,
            n.right,
            n.bottom_left,
            n.bottom,
            n.bottom_right,
        ]:
            if nbr is None:
                continue
            if nbr in visited:
                continue
            visited.add(nbr)
            queue.append(nbr)

    return None


# Funksjon for å finne retningen til et koordinat
#  returnerer en liste med koordinater på formen [x,y]
def findDirection(Graph, startX, startY) -> list[int, int]:
    startNode = Graph[startX][startY]
    # print(startNode)
    targetNode = shortestAlive(Graph, startNode)

    if targetNode is None:
        return [startX, startY]

    targetX = targetNode.xPos
    targetY = targetNode.yPos

    dx = targetX - startX
    dy = targetY - startY

    # prefer moving along the axis with the larger distance
    if abs(dx) >= abs(dy):
        return [startX + (1 if dx > 0 else -1 if dx < 0 else 0), startY]
    else:
        return [startX, startY + (1 if dy > 0 else -1 if dy < 0 else 0)]
