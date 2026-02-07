import pygame
import os

class AudioManager:
    def __init__(self):
        self.base_path = os.path.join("assets", "music")
        self.music_volume = 0.4

    def play_background(self):
        path = os.path.join(self.base_path, "background.mp3")
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1, fade_ms=1500)

    def play_combat(self):
        path = os.path.join(self.base_path, "combat.mp3")
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1, fade_ms=500)

    def stop_music(self, fade_ms=1000):
        pygame.mixer.music.fadeout(fade_ms)
