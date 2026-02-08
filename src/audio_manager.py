import pygame
import os


class AudioManager:
    def __init__(self):
        # Paths
        self.music_path = os.path.join("assets", "music")
        self.sfx_path = os.path.join("assets", "sfx")

        # Volum
        self.music_volume = 0.4
        self.sfx_volume = 0.7

        # -----------------
        # Sound effects
        # -----------------
        self.eat_grass = pygame.mixer.Sound(
            os.path.join(self.sfx_path, "eat_grass.wav")
        )
        self.win_sound = pygame.mixer.Sound(os.path.join(self.sfx_path, "you_win.wav"))
        self.lose_sound = pygame.mixer.Sound(
            os.path.join(self.sfx_path, "you_lose.wav")
        )

        self.eat_grass.set_volume(self.sfx_volume)
        self.win_sound.set_volume(self.sfx_volume)
        self.lose_sound.set_volume(self.sfx_volume)

    # -----------------
    # Background music
    # -----------------
    def play_background(self):
        path = os.path.join(self.music_path, "background.mp3")
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1, fade_ms=1500)

    def stop_music(self, fade_ms=1000):
        pygame.mixer.music.fadeout(fade_ms)

    # -----------------
    # Sound effects
    # -----------------
    def play_eat_grass(self):
        self.eat_grass.play()

    def play_win(self):
        self.win_sound.play()

    def play_lose(self):
        self.lose_sound.play()
