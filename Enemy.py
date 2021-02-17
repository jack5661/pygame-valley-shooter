import pygame
from pygame.locals import *
import Helpers
from Helpers import Direction
from Bound_Detector import Bound_Detector
import random

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

    spawnDirection = Helpers.Direction.UP # Used to determine where to start spawning enemies;
                                          # Start spawning enemies at the top of the map

    def __init__(self, spawn: tuple, speed: int):
        super().__init__()
        self.image = pygame.image.load(Helpers.Assets.ENEMY)
        self.surface = pygame.Surface((22, 22))
        self.rect = self.surface.get_rect()
        self.rect.center = (spawn[0], spawn[1])
        self._speed = speed

    def update(self, playerCoords: tuple):
        if playerCoords is None:
            return

        playerX, playerY = playerCoords
        mobX, mobY = self.rect.center
        if playerX > mobX and Bound_Detector.check(self.rect, self._speed, Direction.RIGHT):
            self.rect.move_ip(self._speed, 0)
        if mobX > playerX and Bound_Detector.check(self.rect, self._speed, Direction.LEFT):
            self.rect.move_ip(-self._speed, 0)
        if playerY > mobY and Bound_Detector.check(self.rect, self._speed, Direction.DOWN):
            self.rect.move_ip(0, self._speed)
        if mobY > playerY and Bound_Detector.check(self.rect, self._speed, Direction.UP):
            self.rect.move_ip(0, -self._speed) 

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
        spawnPoints = cls.SPAWN_DICT[cls.spawnDirection]
        enemies = []
        idx = 0
        adder = lambda x: x * Helpers.GAME_TILE + int(Helpers.GAME_TILE / 2)
        for i in range(num):
            if idx == len(spawnPoints):
                idx = 0
            spawn = spawnPoints[idx]
            spawn = adder(spawn[0]), adder(spawn[1])
            enemies.append(cls(spawn, 1 + idx))
            idx += 1

        cls.spawnDirection = Helpers.Direction.rotateDirection(cls.spawnDirection)
        
        return enemies
