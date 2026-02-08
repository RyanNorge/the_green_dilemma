from email.mime import audio
import pygame
import sys
import time
import random


import temp_rutenett
import node as Node
from audio_manager import AudioManager
from jordrotte import Jordrotte


def run():

    # Initialize pygame
    pygame.init()

    # Set up audio
    audio_manager = AudioManager()
    audio_manager.play_background()

    # Set up the window
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Death")

    # Create game objects
    grid = Node.build_grid(30, 30)
    jordrotte = Jordrotte(screen)

    # Clock to control framerate
    clock = pygame.time.Clock()
    FPS = 60

    # Colors
    DARK_GRAY = (50, 50, 50)

    # Game variables
    x, y = 100, 100
    speed = 5

    audio = AudioManager()
    audio.play_background()

    # Game loop
    running = True
    last_world_update = 0
    last_screen_update = 0
    while running:
        clock.tick(FPS)  # Limit frame rate

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     x -= speed
        # if keys[pygame.K_RIGHT]:
        #     x += speed
        # if keys[pygame.K_UP]:
        #     y -= speed
        # if keys[pygame.K_DOWN]:
        #     y += speed

        # update world
        if time.time() > last_world_update + 1:
            Node.updateAllNodes(grid)

            last_world_update = time.time()

        if time.time() > last_screen_update + 0.5:
            # Update jordrotte sprite
            jordrotte.sprite.next()
            x = random.choice([-1, 0, 0, 1])
            y = random.choice([-1, 0, 0, 1])
            jordrotte.move(x, y)

            # Update display
            screen.fill(DARK_GRAY)
            temp_rutenett.draw(screen, grid)
            jordrotte.draw(screen)
            pygame.display.flip()

            last_screen_update = time.time()

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
