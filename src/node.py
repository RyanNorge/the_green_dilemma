class Node:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.isAlive = False
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None



def build_grid(width, height):

    # Create nodes
    grid = []
    for x in range(width):
        grid.append([])
        for y in range(height):
            grid[x].append(Node(x, y))

    #Helper to get node or None
    def get(x, y):
        if 0 <= x < width and 0 <= y < height:
            return grid[y][x]
        return None
    

    #Link neighbors
    for y in range(height):
        for x in range(width):
            node = grid[y][x]
            node.top = get(x, y-1)
            node.bottom = get(x, y+1)
            node.left = get(x-1, y)
            node.right = get(x+1, y)
            node.top_left = get(x-1, y-1)
            node.top_right = get(x+1, y-1)
            node.bottom_left = get(x-1, y+1)
            node.bottom_right = get(x+1, y+1)
    return grid

