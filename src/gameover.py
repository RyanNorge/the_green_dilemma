import pygame
from audio_manager import AudioManager


class GameOver:
    WIN_COLOR = (0, 200, 0)
    LOSE_COLOR = (200, 0, 0)
    FONT_SIZE = 48

    def __init__(self, screen: pygame.Surface, audio: AudioManager):
        self.screen = screen
        self.audio = audio
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)
        self.finished = False

    def check(self, grid):
        total_cells = len(grid) * len(grid[0])
        grass_cells = sum(1 for row in grid for node in row if node.isAlive)

        coverage = grass_cells / total_cells

        if coverage >= 0.7 and not self.finished:
            self.finished = True
            self.audio.stop_music()
            self.audio.play_win()
            self.display_message("YOU WIN", self.WIN_COLOR)
            return "WIN"

        elif grass_cells == 0 and not self.finished:
            self.finished = True
            self.audio.stop_music()
            self.audio.play_lose()
            self.display_message("YOU LOSE", self.LOSE_COLOR)
            return "LOSE"

        return None

    def display_message(self, text, color):
        overlay = pygame.Surface(self.screen.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        rendered = self.font.render(text, True, color)
        rect = rendered.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(rendered, rect)

        pygame.display.flip()
