import pygame

import audio_manager


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

        # starting location
        self.x = 5
        self.y = 5
        self.speed = 5
        self.screen = screen
        self.sprite = Sprite()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return

    def draw(self, screen: pygame.Surface):
        screen.blit(
            self.sprite.get(),
            (
                self.x * 50 - 25,
                self.y * 50 - 25,
            ),
        )

    def play_eat_grass(self):
        audio_manager.AudioManager.play_eat_grass()
