import pygame
import os


class AudioManager:
    def __init__(self):
        self.base_path = os.path.join("assets", "music")
        self.sfx_path = os.path.join("assets", "sfx")

#-------Init Mixer-------   
        pygame.mixer.init()


        self.music_volume = 0.4
        self.sfx_volume = 0.6

        # later inn SFX en gang

        eat_path = os.path.join(self.sfx_path, "eat_grass.wav")
        self.eat_grass = pygame.mixer.Sound(eat_path)
        self.eat_grass.set_volume(self.sfx_volume)


#-----------Bakgrunnsmusikk-------

    def play_background(self):
        path = os.path.join(self.base_path, "background.mp3")
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1, fade_ms=1500)


    def stop_music(self, fade_ms=1000):
        pygame.mixer.music.fadeout(fade_ms)

    def play_eat_grass(self):
        self.eat_grass.play()

