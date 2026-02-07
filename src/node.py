class Node:
    def __init__(self, xPos, yPos, alive):
        self.xPos = xPos
        self.yPos = yPos
        self.isAlive = alive
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

    # Helper to get node or None
    def get(x, y):
        if 0 <= x < width and 0 <= y < height:
            return grid[y][x]
        return None
    # Link neighbors
    for y in range(height):
        for x in range(width):
            n = grid[y][x]
            n.top = get(x, y-1)
            n.bottom = get(x, y+1)
            n.left = get(x-1, y)
            n.right = get(x+1, y)
            n.top_left = get(x-1, y-1)
            n.top_right = get(x+1, y-1)
            n.bottom_left = get(x-1, y+1)
            n.bottom_right = get(x+1, y+1)
    return grid

