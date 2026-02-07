import pygame
import sys
import time


import temp_rutenett
import node as Node


def run():

    # Initialize pygame
    pygame.init()

    # Set up the window
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Death")

    # Create game objects
    grid = Node.build_grid(30, 30)

    # Clock to control framerate
    clock = pygame.time.Clock()
    FPS = 60

    # Colors
    WHITE = (255, 255, 255)
    DARK_GRAY = (50, 50, 50)
    BLUE = (60, 60, 255)

    # Game variables
    x, y = 100, 100
    speed = 5
    size = 50

    # Game loop
    running = True
    last_update = 0
    while running:
        clock.tick(FPS)  # Limit frame rate

        # update world every 1 sec
        if time.time() > last_update + 1:
            # if False:
            # grid = Node.build_grid(30, 30)

            # update nodes
            for row in grid:
                for node in row:
                    node.checkNextUpdate()
            for row in grid:
                for node in row:
                    node.updateStatus()

            last_update = time.time()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        # Draw
        screen.fill(DARK_GRAY)

        # Update display
        temp_rutenett.draw(screen, grid)

        pygame.display.flip()

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
