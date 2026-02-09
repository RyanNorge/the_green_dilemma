import pygame
import time
import random

import grid
import node
from grid import Grid
from screen import Screen
from jordrotte import Jordrotte
from audio_manager import AudioManager
from gameover import GameOver

GRID_WIDTH, GRID_HEIGHT = 22, 12


class State:
    def __init__(
        self, num_jordrotter: int, screen: Screen, audio_manager: AudioManager
    ) -> None:

        self.num_jordrotter = num_jordrotter
        self.screen = screen
        self.audio_manager = audio_manager
        self.audio_manager.play_background()

        self.gameover = GameOver(screen, audio_manager)

        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)

        # self.jordrotte = Jordrotte(self.screen)
        self.mange_jordrotter: list[Jordrotte] = []
        for _ in range(self.num_jordrotter):
            self.mange_jordrotter.append(
                Jordrotte(self.screen, GRID_WIDTH, GRID_HEIGHT)
            )

        # self.screen.set_objects(self.grid, self.jordrotte)
        self.screen.set_objects(self.grid, self.mange_jordrotter)

        self.clock = pygame.time.Clock()
        self.FPS = 8

        self.last_grass_update = 0
        self.last_jordrotte_update = 0
        self.last_screen_update = 0

        # go though some generations to get the right pattern going
        for _ in range(4):
            self.forced_next()

    def next(self, render=True) -> None:

        # Limit frame rate
        self.clock.tick(self.FPS)
        time_now = time.time()

        # Update jordrotte sprite
        jordrotte_interval = 0.5
        if time_now > self.last_jordrotte_update + jordrotte_interval:
            for jord in self.mange_jordrotter:
                jord.sprite.next()

                nextCoordinate = node.findDirection(self.grid.cells, jord.x, jord.y)
                # randomize their movement a bit
                # this is becuase if two sprites land on the same tile,
                # they will always move in the same direction at the same time,
                # and essentially become one jordrotte instead of two.
                # this is a lazy way to fix that.
                if random.random() <= 0.2:
                    for i, this_coor in enumerate(nextCoordinate):
                        if this_coor == 0:
                            nextCoordinate[i] += 1
                        elif this_coor >= min(GRID_HEIGHT, GRID_HEIGHT) - 1:
                            nextCoordinate[i] -= 1
                        else:
                            nextCoordinate[i] += random.choice((1, -1))
                jord.move(nextCoordinate[0], nextCoordinate[1])
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
        if time_now > self.last_screen_update + screen_update_interval and render:
            self.screen.render()
            self.last_screen_update = time_now

    def forced_next(self):
        """Force advancing state by resetting last update times."""

        self.last_grass_update = 0
        self.last_jordrotte_update = 0
        self.last_screen_update = 0
        self.next(render=False)

    def checkEating(self):
        for jord in self.mange_jordrotter:
            jord: Jordrotte

            if self.grid.cells[jord.x][jord.y].isAlive:
                self.grid.cells[jord.x][jord.y].changeAliveStatus(False)
                self.audio_manager.play_eat_grass()
