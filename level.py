# level.py
import pygame
from settings import *
from enemy import Enemy

class Level:
    def __init__(self, player):
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = player
        self.load_level()

    def load_level(self):
        # Add playforms
        for i in range(0, WIDTH, 100):
            platform = pygame.Surface((100, 20))
            platform.fill(BLUE)
            platform_rect = platform.get_rect()
            platform_rect.x = i
            platform_rect.y = HEIGHT - 40
            self.platforms.add(pygame.sprite.Sprite())
            self.platforms.sprites()[-1].image = platform
            self.platforms.sprites()[-1].rect = platform_rect

        # Add emenies
        for i in range(200, WIDTH, 400):
            enemy = Enemy(i, HEIGHT - 60)
            self.enemies.add(enemy)

    def update(self):
        self.platform.update()
        self.enemies.update()

    def draw(self, screen):
        self.platforms.draw(screen)
        self.enemies.draw(screen)