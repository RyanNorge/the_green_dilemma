import pygame
import sys
import random

# Initialiser pygame
pygame.init()

# Skjermstørrelse
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life - Startmeny")

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
DARK_GREEN = (0, 150, 0)
LIGHT_GREEN = (100, 255, 100)
CELL_COLOR = (0, 200, 0, 100)

# Font
base_font_size = 40

# Knappklasse med vekst
class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.hover_color = hover_color
        self.scale = 1.0
        self.hover_scale = 1.1

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Mus over knapp
        if self.x < mouse[0] < self.x + self.w and self.y < mouse[1] < self.y + self.h:
            target_scale = self.hover_scale
            if click[0] == 1:
                return True
        else:
            target_scale = 1.0

        # Smooth vekst
        self.scale += (target_scale - self.scale) * 0.1

        # Skaler knapp
        scaled_w = int(self.w * self.scale)
        scaled_h = int(self.h * self.scale)
        scaled_x = self.x + (self.w - scaled_w)//2
        scaled_y = self.y + (self.h - scaled_h)//2

        pygame.draw.rect(screen, self.hover_color if self.scale > 1.05 else self.color,
                         (scaled_x, scaled_y, scaled_w, scaled_h), border_radius=10)

        # Tekst
        text_surf = pygame.font.SysFont(None, int(base_font_size * self.scale)).render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=(scaled_x + scaled_w//2, scaled_y + scaled_h//2))
        screen.blit(text_surf, text_rect)

        return False

# Celleklasse for bakgrunn
class Cell:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(2, 5)
        self.growth_rate = random.uniform(0.05, 0.2)

    def grow(self):
        self.size += self.growth_rate
        if self.size > 10:
            self.size = random.randint(2, 5)
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), int(self.size))

def main_menu():
    start_button = Button("Start Game", 200, 150, 200, 60, LIGHT_GREEN, DARK_GREEN)
    quit_button = Button("Quit", 200, 250, 200, 60, LIGHT_GREEN, DARK_GREEN)

    # Lag bakgrunnsceller
    cells = [Cell() for _ in range(50)]

    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(WHITE)

        # Oppdater og tegn celler
        for cell in cells:
            cell.grow()
            cell.draw(screen)

        # Tittel
        title_font = pygame.font.SysFont(None, 60)
        title_surf = title_font.render("Game of Life", True, GREEN)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 80))
        screen.blit(title_surf, title_rect)

        # Tegn knapper
        if start_button.draw():
            print("Spillet starter...")  # Her starter du Game of Life
            running = False
        if quit_button.draw():
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main_menu()
