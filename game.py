# game.py
import pygame
from settings import *
from player import Player
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Simple Platformer")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.level = Level(self.player)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.all_sprites.add(self.level.platforms)
        self.all_sprites.add(self.level.enemies)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollide(self.player, self.level.enemies, False):
            print("Game Over")
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.level.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def main(self):
        while True:
            self.run()

if __name__ == "__main__":
    game = Game()
    game.main()
