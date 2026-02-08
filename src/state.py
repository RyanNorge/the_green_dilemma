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
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        self.screen = Screen(GRID_WIDTH, GRID_HEIGHT)
        self.jordrotte = Jordrotte(self.screen)

        self.screen.set_objects(self.grid, self.jordrotte)

        self.clock = pygame.time.Clock()
        self.FPS = 8

        self.last_grass_update = 0
        self.last_jordrotte_update = 0
        self.last_screen_update = 0

    def next(self) -> None:

        # Limit frame rate
        self.clock.tick(self.FPS)
        time_now = time.time()

        # Update jordrotte sprite
        jordrotte_interval = 0.5
        if time_now > self.last_jordrotte_update + jordrotte_interval:
            self.jordrotte.sprite.next()

            nextCoordinate = node.findDirection(
                self.grid.cells, self.jordrotte.x, self.jordrotte.y
            )
            self.jordrotte.move(nextCoordinate[0], nextCoordinate[1])
            self.last_jordrotte_update = time.time()

        # update grass
        grass_update_interval = 2.5
        if time_now > self.last_grass_update + grass_update_interval:
            node.updateAllNodes(self.grid.cells)
            self.last_grass_update = time_now

        # eat grass if on grass tile
        self.checkEating()

        # update screen
        screen_update_interval = 1 / 2
        if time_now > self.last_screen_update + screen_update_interval:
            self.screen.render()
            self.last_screen_update = time_now

    def checkEating(self):
        if self.grid.cells[self.jordrotte.x][self.jordrotte.y].isAlive:
            self.grid.cells[self.jordrotte.x][self.jordrotte.y].changeAliveStatus(False)

        # self.jordrotte.play_eat_grass()
