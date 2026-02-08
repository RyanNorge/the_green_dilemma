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

    # Game loop
    running = True
    while running:
        state.next()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
