import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.music_volume = 0.5

    def play_music(self, path, loop = True, fade_ms=1000): 
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume) 
        pygame.mixer.music.play(-1 if loop else 0, fade_ms=fade_ms)     

    def stop_music(self, fade_ms=1000):
        pygame.mixer.music.fadeout(fade_ms)

    def set_music_volume(self, volume):
        self.music_volume = max(0.0, min(1.0, volume))  # Clamp between 0.0 and 1.0
        pygame.mixer.music.set_volume(self.music_volume)