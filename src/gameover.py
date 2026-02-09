import pygame
from typing import Literal
import random

from audio_manager import AudioManager
from grid import Grid
from node import Node
from screen import Screen

STUPID_COMPLEMENTS = (
    "You are so effing smart!",
    "You're, like, a genious!",
    "You win a prize or something!",
    "Your mom must be so proud!",
    "You accomplished soemthing really important!",
    "This is a good use of your time!",
    "Good looking people will like you now!",
    "Someone gives you money! Good job!",
    "You saved the day! And the planet! And some kittens!",
    "Your friends give you their approval!",
)

STUPID_INSULTS = (
    "Man, you must be so ashamed of yourself!",
    "Wow, what an idiot! And a looser!",
    "You are stupid. Your friends are gonna laugh at you.",
    "If you've failed at this, I hate to think \n how the rest of your life must be going!",
)

STUPID_RECCOMENDATIONS = (
    "You should go think about all your failures before trying again.",
    "Maybe you should quit and never try hard things again.",
    "Find a new hobby. Seems video games are not for you.",
)


class GameOver:
    WIN_COLOR = (0, 200, 0)
    LOSE_COLOR = (200, 0, 0)
    FONT_SIZE = 48

    def __init__(self, screen: Screen, audio: AudioManager):
        self.screen = screen
        self.audio = audio
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)
        self.finished = False

    def check(self, grid: Grid) -> Literal["win", "lose", "continue"]:

        total_cells = grid.height * grid.width

        grass_cells = 0
        for row in grid.cells:
            for this_node in row:
                this_node: Node
                if this_node.isAlive:
                    grass_cells += 1

        coverage = grass_cells / total_cells
        grid.coverage = coverage
        # print(coverage)

        if coverage >= 0.7 and not self.finished:
            print(f"game ending. WON with coverage: {coverage}")
            self.finished = True
            self.audio.stop_music()
            self.audio.play_win()
            self.display_message(
                f"70% grass alive!\n\n"
                f"{random.choice(STUPID_COMPLEMENTS)}\n\n"
                "now more jordrotter...\n",
                self.WIN_COLOR,
            )
            pygame.time.delay(3000)
            return "win"

        if coverage <= 0.2 and not self.finished:
            print(f"game ending. LOST with coverage: {coverage}")
            self.finished = True
            self.audio.stop_music()
            self.audio.play_lose()
            self.display_message(
                "Less than 20 percent grass."
                "YOU LOSE!!!!!!!!!\n\n"
                f"{random.choice(STUPID_INSULTS)}\n\n"
                f"{random.choice(STUPID_RECCOMENDATIONS)}\n\n",
                self.LOSE_COLOR,
            )
            pygame.time.delay(6000)
            return "lose"

        return "continue"

    def display_message(self, text, color):
        overlay = pygame.Surface(self.screen.surface.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.surface.blit(overlay, (0, 0))

        rendered = self.font.render(text, True, color)
        rect = rendered.get_rect(center=self.screen.surface.get_rect().center)
        self.screen.surface.blit(rendered, rect)

        pygame.display.flip()
