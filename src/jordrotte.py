import pygame

import audio_manager


GRID_SIZE = 25

# TODO FIX THIS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

CELL_SIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) // GRID_SIZE

WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

OFFSET_X = (SCREEN_WIDTH - WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - HEIGHT) // 2


class Sprite:
    def __init__(self) -> None:

        # load sprites
        idle = pygame.image.load("assets/Jordrotte.png")
        eating = pygame.image.load("assets/Jordrotte_Attack.png")

        self.sprites = [idle, eating]
        self._current_index = 0

        sprite_width, sprite_height = idle.get_size()

        for i, sprite in enumerate(self.sprites):
            self.sprites[i] = pygame.transform.scale(
                sprite, (sprite_width * 2, sprite_height * 2)
            )

    def next(self) -> None:
        # loop index over list of sprites
        self._current_index = (self._current_index + 1) % len(self.sprites)

    def get(self) -> pygame.Surface:
        return self.sprites[self._current_index]


class Jordrotte:
    def __init__(self, screen: pygame.Surface):
        self.x = 50
        self.y = 50
        self.speed = 5
        self.screen = screen
        self.sprite = Sprite()

    def move(self, dx, dy):
        self.x += dx * 50
        self.y += dy * 50
        return

        # this would keep the guy in the screen
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.x = new_x
            self.y = new_y

    def draw(self, screen: pygame.Surface):
        # self.sprite.next()
        screen.blit(
            self.sprite.get(),
            (
                self.x,
                self.y,
            ),
        )

    def play_combat_sound(self):
        audio_manager.AudioManager.play_combat()
