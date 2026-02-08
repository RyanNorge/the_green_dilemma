from email.mime import audio
import pygame
import sys
import time
import random


import grid as Grid
import node as Node
from audio_manager import AudioManager
from jordrotte import Jordrotte
from screen import Screen
from state import State


def run():

    # Initialize pygame
    pygame.init()

    # Set up audio
    audio_manager = AudioManager()
    audio_manager.play_background()

    # Create game objects
    state = State()
    Grid = state.grid

    # Game loop
    running = True
    while running:
        state.next()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse and clicked tile
                mouseX, mouseY = event.pos
                tileX = mouseX // state.screen.cell_size
                tileY = mouseY // state.screen.cell_size

                # Ensure click is inside the grid
                if 0 <= tileX < state.grid.width and 0 <= tileY < state.grid.height:
                    if event.button == 3:
                        print("Mouse clicked at ", tileX, tileY)
                        Grid.cells[tileX][tileY].fertilize()

                    elif event.button == 1:
                        print("Jordrotte fanget")

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
