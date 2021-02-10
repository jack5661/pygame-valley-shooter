import pygame
import random
from pygame.locals import *
import Helpers

class Enemy(pygame.sprite.Sprite):
    
    TOP_SPAWN = ((5, 0), (6, 0), (7, 0))
    RIGHT_SPAWN = ((12, 3), (12, 4))
    BOTTOM_SPAWN = ((5, 7), (6, 7), (7, 7))
    LEFT_SPAWN = ((0, 3), (0, 4))

    SPAWN_POINTS = ( TOP_SPAWN + RIGHT_SPAWN + BOTTOM_SPAWN + LEFT_SPAWN)

    SPAWN_DICT = {Helpers.Direction.UP: TOP_SPAWN,
                  Helpers.Direction.RIGHT: RIGHT_SPAWN,
                  Helpers.Direction.DOWN: BOTTOM_SPAWN,
                  Helpers.Direction.LEFT: LEFT_SPAWN}

    spawnDirection = Helpers.Direction.UP # Star spawning enemies at the top of the map

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
    
    """
    Spawn enemies at spawnpoint
    @param num - Number of enemies to spawn, should be 1 - 3

    Use cls.spawnDirection to determine where to spawn
    Speed of spawn should be determined in App???
    """
    @classmethod
    def spawnEnemy(cls, num: int) -> list:
        pass