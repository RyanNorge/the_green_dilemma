import pygame

from jordrotte import Jordrotte
from grid import Grid

# Colors
DARK_GRAY = (50, 50, 50)


class Screen:
    def __init__(self) -> None:
        # Set up the window
        self.grid: Grid
        self.width = 800
        self.height = 600
        self.cell_size = 50
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Death")

    def draw_jordrotte(jordrotte: Jordrotte) -> None: ...

    def set_objects(self, grid: Grid, jordrotte: Jordrotte) -> None:
        self.grid = grid
        self.jordrotte = jordrotte

    def render(self) -> None:

        # Update display
        self.surface.fill(DARK_GRAY)
        self.grid.draw(self.surface)

        self.jordrotte.draw(self.surface)
        pygame.display.flip()
