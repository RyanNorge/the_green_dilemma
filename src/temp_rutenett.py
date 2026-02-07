import pygame
import random

x = 30
y = 30

ALVIE = (255, 255, 255)
DEAD = (0, 0, 0)


def build_grid(width, height, cell_size):
    grid = []
    for row in range(0, height, cell_size):
        grid_row = []
        for col in range(0, width, cell_size):
            grid_row.append(random.choice([True, False]))
        grid.append(grid_row)
    return grid


def draw(screen, grid):
    for this_x, row in enumerate(grid):
        for this_y, cell in enumerate(row):
            pygame.draw.rect(
                screen,
                ALVIE if cell else DEAD,
                pygame.Rect(this_y * 10, this_x * 10, 10, 10),
                width=5,
            )
