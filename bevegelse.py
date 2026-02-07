import pygame
import sys

# -----------------
# INIT
# -----------------

pygame.init()

# FULLSCREEN
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

GRID_SIZE = 25

CELL_SIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) // GRID_SIZE

WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

OFFSET_X = (SCREEN_WIDTH - WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - HEIGHT) // 2


FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption("Grid Movement")

# Colors
BG_COLOR = (30, 30, 30)
GRID_COLOR = (60, 60, 60)

# -----------------
# LOAD PLAYER IMAGE
# -----------------

jordrotte_img = pygame.image.load("jordrotte.png").convert_alpha()
jordrotte_img = pygame.transform.scale(jordrotte_img, (CELL_SIZE, CELL_SIZE))

# ------------------
# CHARACTER CLASS
# ------------------


class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        surface.blit(
            self.image,
            (
                OFFSET_X + self.x * CELL_SIZE,
                OFFSET_Y + self.y * CELL_SIZE,
            ),
        )


# ------------------
# DRAW GRID
# ------------------


def draw_grid(surface):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(
                OFFSET_X + x * CELL_SIZE,
                OFFSET_Y + y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)


# ------------------
# MAIN LOOP
# ------------------

player = Character(GRID_SIZE // 2, GRID_SIZE // 2, jordrotte_img)

move_delay = 120
last_move_time = 0

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ESC to exit fullscreen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    now = pygame.time.get_ticks()

    if now - last_move_time > move_delay:
        if keys[pygame.K_w]:
            player.move(0, -1)
            last_move_time = now
        elif keys[pygame.K_s]:
            player.move(0, 1)
            last_move_time = now
        elif keys[pygame.K_a]:
            player.move(-1, 0)
            last_move_time = now
        elif keys[pygame.K_d]:
            player.move(1, 0)
            last_move_time = now

    screen.fill(BG_COLOR)
    draw_grid(screen)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
