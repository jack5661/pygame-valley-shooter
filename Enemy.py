import pygame
import random
from pygame.locals import *
import Helpers

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Helpers.ASSETS + "enemy.png")
        self.surface = pygame.Surface((22, 22))
        self.rect = self.surface.get_rect()
        x, y = random.randrange(0, Helpers.GAME_WIDTH), random.randrange(0, Helpers.GAME_HEIGHT)
        self.rect.center = (x, y)
        self._speed = 3

    def update(self):
        dir = random.randrange(0, 4)
        if dir == 0: # UP
            self.rect.move_ip(0, -self._speed)
        elif dir == 1: # RIGHT
            self.rect.move_ip(self._speed, 0)
        elif dir == 2: # DOWN
            self.rect.move_ip(0, self._speed)
        else: # LEFT
            self.rect.move_ip(-self._speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)