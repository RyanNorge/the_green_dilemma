import pygame


class Player:
    def __init__(self):

        # Game variables
        self.x, self.y = 300, 300
        self.speed = 5
        self.size = 50
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.sprite = pygame.image.load("assets/sans.png")

    def move(self, keys):
        # Get key presses
        # keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Draw
        RED = (255, 0, 0)

        # pygame.draw.rect(RED, (self.x, self.y, self.size, self.size))
        self.rect.move(self.x, self.y)
