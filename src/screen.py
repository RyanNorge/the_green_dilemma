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

        self.overlay = pygame.Surface(self.surface.get_size())
        self.coverage_font = pygame.font.SysFont("Arial", 30)
        self.coverage_box = pygame.Rect()

        # self.overlay.set_alpha()

    def set_objects(self, grid: Grid, mange_jordrotter: list[Jordrotte]) -> None:
        self.grid = grid
        self.mange_jordrotter = mange_jordrotter

    def render(self) -> None:

        # build frame
        self.surface.fill(DARK_GRAY)
        self.grid.draw(self.surface)
        for jord in self.mange_jordrotter:
            jord.draw(self.surface)
        self.show_coverage()

        # display frame
        pygame.display.flip()

    def show_coverage(self):
        lum = 16
        color = pygame.color.Color(lum, lum, lum)
        # pygame.draw.rect(self.surface, color, pygame.Rect(15, 15, 300, 65))
        box = pygame.Surface((285, 48))
        box.set_alpha(128)
        box.fill(color)
        self.surface.blit(box, (18, 18))

        self.surface.blit(
            self.coverage_font.render(
                f"Grass Coverage: {int(self.grid.coverage * 100)}",
                True,
                (255, 255, 255),
            ),
            (25, 25),
        )
