import pygame

from node import Node
from node import build_grid


ALIVE_SPRITE = pygame.image.load("assets/GrassTile.png")
DEAD_SPRITE = pygame.image.load("assets/DirtTile.png")


class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.cell_size = 50
        self.cells = build_grid(width, height)
        self.coverage = 0.6

    def get_cell(self, x, y) -> Node:
        """X is width, Y is height, starting from upper left corner."""
        return self.cells[x][y]

    def draw(self, screen: pygame.Surface):
        for this_x, row in enumerate(self.cells):
            for this_y, cell in enumerate(row):
                cell: Node
                cell.updateSprite()
                sprite = cell.getSprite()

                # scale sprite to the configured cell size (keep tiles at 50x50)
                scaled = pygame.transform.scale(
                    sprite, (self.cell_size, self.cell_size)
                )

                # grid is indexed as grid[x][y] where x=column, y=row
                screen.blit(scaled, (self.cell_size * this_x, self.cell_size * this_y))


# just making it obvious that we are using the method from Node here
build_grid = build_grid
