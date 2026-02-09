import pygame
import sys
import time
import random
from gameover import GameOver


import grid as Grid
import node as Node
from audio_manager import AudioManager
from jordrotte import Jordrotte
from screen import Screen
from state import State


def run():

    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Set up screen and audio
    screen = pygame.display.set_mode((800, 600))
    audio_manager = AudioManager()
    audio_manager.play_background()
    gameover = GameOver(screen, audio_manager)

    # Opprett Game Over

    # Create game objects
    state = State()
    Grid = state.grid
    Jordrotte = state.jordrotte

    # go though a couple of generations to get the right pattern going
    state.next()
    state.next()

    # Game loop
    running = True
    last_ending_check = time.time()
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

                    # Right click to trap the jordrotte
                    if event.button == 1:
                        if tileX == Jordrotte.x and tileY == Jordrotte.y:
                            print("Jordrotte fanget")
                            Jordrotte.trap()

                        # Right click: move the jordrotte to clicked tile
                        # state.jordrotte.move(tileX, tileY)
                        # print(f"Moved jordrotte to {tileX},{tileY}")
        # Game over

        # Sjekke Game Over
        now_time = time.time()
        if now_time > last_ending_check + 2:
            game_has_ended = gameover.check(Grid)
            running = not game_has_ended
            last_ending_check = now_time

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
