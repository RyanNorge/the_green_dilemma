import pygame
import sys
import time
import random
from gameover import GameOver


from grid import Grid
from audio_manager import AudioManager
from jordrotte import Jordrotte
from screen import Screen
from state import State


GRID_WIDTH, GRID_HEIGHT = 22, 12


def create_new_state(oldstate: None | State = None): ...


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
    # grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    screen = Screen(GRID_WIDTH, GRID_HEIGHT)

    state = State(2, screen, audio_manager)

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
                    if event.button == 1:
                        # print("Mouse clicked at ", tileX, tileY)
                        state.grid.cells[tileX][tileY].fertilize()

                        for jord in state.mange_jordrotter:
                            # click on the jordrotte to trap it
                            if tileX == jord.x and tileY == jord.y:
                                # print("Jordrotte fanget")
                                jord.trap()

        # Sjekke Game Over
        if time.time() > last_ending_check + 1:
            game_over_state = state.gameover.check(state.grid)

            if game_over_state == "win":
                state = State(state.num_jordrotter * 2, screen, audio_manager)
            elif game_over_state == "lose":
                running = False
            last_ending_check = time.time()

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
