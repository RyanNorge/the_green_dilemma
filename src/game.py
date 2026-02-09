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

    # Opprett Game Over

    # Create game objects
    state = State()
    Grid = state.grid
    Jordrotte = state.jordrotte
    gameover = GameOver(screen, audio_manager)

    # Game loop
    running = True
    last_end_check = time.time()
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

                    # Right click: move the jordrotte to clicked tile
                    elif event.button == 3:
                        state.jordrotte.move(tileX, tileY)
                        print(f"Moved jordrotte to {tileX},{tileY}")

        # pygame.time.delay(1000)

        # Sjekke Game Over
        now_time = time.time()
        if now_time > last_end_check + 2:
            is_game_over = gameover.check(Grid)
            running = not is_game_over
            last_end_check = now_time

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
