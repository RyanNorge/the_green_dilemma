import pygame

from jordrotte import Jordrotte
from grid import Grid

# Colors
DARK_GRAY = (50, 50, 50)


class Screen:
    def __init__(self, width, height) -> None:
        # Set up the window
        self.grid: Grid
        self.cell_size = 50
        self.width = width * self.cell_size
        self.height = height * self.cell_size

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Death")

    def set_objects(self, grid: Grid, mange_jordrotter: list[Jordrotte]) -> None:
        self.grid = grid
        self.mange_jordrotter = mange_jordrotter

    def render(self) -> None:

        # build frame
        self.surface.fill(DARK_GRAY)
        self.grid.draw(self.surface)
        for jord in self.mange_jordrotter:
            jord.draw(self.surface)

        # display frame
        pygame.display.flip()
