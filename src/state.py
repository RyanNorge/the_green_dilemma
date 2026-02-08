import pygame
import time
import random

import grid
import node
from grid import Grid
from screen import Screen
from jordrotte import Jordrotte

GRID_WIDTH, GRID_HEIGHT = 16, 12


class State:
    def __init__(self) -> None:
        # self.grid = grid.build_grid(GRID_WIDTH, GRID_HEIGHT)
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        self.screen = Screen(GRID_WIDTH, GRID_HEIGHT)
        self.jordrotte = Jordrotte(self.screen)

        self.screen.set_objects(self.grid, self.jordrotte)

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.last_grass_update = 0
        self.last_screen_update = 0
        self.last_jordrotte_update = 0

    def next(self) -> None:
        self.clock.tick(self.FPS)  # Limit frame rate

        # Update jordrotte sprite
        jordrotte_interval = 0.5
        if time.time() > self.last_jordrotte_update + jordrotte_interval:
            self.jordrotte.sprite.next()

            nextCoordinate = node.findDirection(
                self.grid.cells, self.jordrotte.x, self.jordrotte.y
            )
            self.jordrotte.move(nextCoordinate[0], nextCoordinate[1])
            self.last_jordrotte_update = time.time()

        grass_update_interval = 1
        if time.time() > self.last_grass_update + grass_update_interval:
            node.updateAllNodes(self.grid.cells)
            self.last_grass_update = time.time()

        self.screen.render()

    def checkEating(self):
        if self.grid.cells[self.jordrotte.x][self.jordrotte.y].isAlive:
            self.grid.cells[self.jordrotte.x][self.jordrotte.y].changeAliveStatus(False)

        print(self.jordrotte.x, self.jordrotte.y)
