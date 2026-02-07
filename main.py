import subprocess
from audio import AudioManager


# For audio playback
pygame.init()
pygame.mixer.init()

audio = AudioManager()
audio.play_background()



def main():

    # Format code with ruff
    subprocess.run(["uv", "run", "ruff", "format"])

    # Run the game with environment loaded
    subprocess.run(["uv", "run", "src/game.py"])


if __name__ == "__main__":
    main()

var = 0
while var != 10:
    var += 1
    print("hei")

    # --- Lyd --- test

# import os
# hit_sound_path = os.path.join(os.path.dirname(__file__), "sounds", "hit.wav")
# hit_sound = pygame.mixer.Sound(hit_sound_path) if os.path.exists(hit_sound_path) else None
# if hit_sound:
#    hit_sound.set_volume(0.5)

# game_over_sound_path = os.path.join(os.path.dirname(__file__), "sounds", "game_over.wav")
# game_over_sound = pygame.mixer.Sound(game_over_sound_path) if os.path.exists(game_over_sound_path) else None
# if game_over_sound:
# game_over_sound.set_volume(0.5)
# running = True

# Pause skjerm
#   if game_state == PAUSED:
#       paused_text = font_big.render("PAUSED", True, THEME["text_color"])
#       hint_text = font_small.render("Press P to continue", True, THEME["text_color"])
#       screen.blit(paused_text, (WIDTH // 2 - 120, HEIGHT // 2 - 60))
#       screen.blit(hint_text, (WIDTH // 2 - 140, HEIGHT // 2 + 10))


# Restart
#            if event.key == pygame.K_r and game_state == GAME_OVER:
#               game_state = PLAYING
#               player = Player()
#               score = Score()
#               obstacles.clear()
#               spawn_timer = 0
#               obstacle_speed = 4
#               difficulty_timer = 0
#               lives = 3
#               if game_over_sound:
#                   game_over_sound.stop()


# Game Over skjerm
#   if game_state == GAME_OVER:
#       game_over_text = font_big.render("GAME OVER", True, THEME["text_color"])
#       score_text = font_small.render(f"Score: {score.value}", True, THEME["text_color"])
#       restart_text = font_small.render("Press R to Restart", True, THEME["text_color"])
#       screen.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 60))
#       screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))
#       screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 40))

# class Obstacle:
#    def __init__(self, base_speed):
# Velg tilfeldig størrelse på hindringen
#        self.size = random.choice([30, 40, 50, 60])  # små, medium, store
#        # Litt variasjon i hastigheten
#        self.speed = base_speed + random.choice([-1, 0, 1])
# Start x-posisjon tilfeldig
#        x = random.randint(0, WIDTH - self.size)
#        # Lag pygame.Rect for hindringen
#        self.rect = pygame.Rect(x, -self.size, self.size, self.size)

#    def update(self):
# Flytt hindringen nedover
#        self.rect.y += self.speed

#    def draw(self, screen):
#        # Tegn hindringen som et rektangel
#        pygame.draw.rect(screen, THEME["obstacle_color"], self.rect)
#
#    def off_screen(self):

#        # Sjekk om hindringen har passert skjermen
#        return self.rect.top > HEIGHT
