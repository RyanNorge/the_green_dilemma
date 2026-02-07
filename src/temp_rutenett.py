import pygame
import random


x = 30
y = 30

ALVIE = (255, 255, 255)
DEAD = (0, 0, 0)

ALIVE_SPRITE = pygame.image.load("assets/GrassTile.png")
DEAD_SPRITE = pygame.image.load("assets/DirtTile.png")


def build_grid(width, height, cell_size):
    grid = []
    for row in range(0, height, cell_size):
        grid_row = []
        for col in range(0, width, cell_size):
            grid_row.append(random.choice([True, False]))
        grid.append(grid_row)
    return grid


def draw(screen: pygame.Surface, grid):
    for this_x, row in enumerate(grid):
        for this_y, cell in enumerate(row):
            (
                screen.blit(
                    # ALIVE_SPRITE if cell else DEAD_SPRITE, (this_y * 10, this_x * 10)
                    ALIVE_SPRITE if cell.isAlive else DEAD_SPRITE,
                    (
                        DEAD_SPRITE.get_height() * this_y,
                        DEAD_SPRITE.get_width() * this_x,
                    ),
                ),
            )
