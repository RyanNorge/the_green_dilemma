import pygame

from node import Node
from node import build_grid


ALIVE_SPRITE = pygame.image.load("assets/GrassTile.png")
DEAD_SPRITE = pygame.image.load("assets/DirtTile.png")


class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.cells = build_grid(width, height)

    def get_cell(self, x, y) -> Node:
        """X is width, Y is height, starting from upper left corner."""
        return self.cells[x][y]

    def draw(self, screen: pygame.Surface):
        for this_x, row in enumerate(self.cells):
            for this_y, cell in enumerate(row):
                cell: Node
                screen.blit(
                    ALIVE_SPRITE if cell.isAlive else DEAD_SPRITE,
                    (
                        DEAD_SPRITE.get_height() * this_y,
                        DEAD_SPRITE.get_width() * this_x,
                    ),
                )


# just making it obvious that we are using the method from Node here
build_grid = build_grid
