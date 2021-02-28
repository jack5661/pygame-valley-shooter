import pygame
from pygame.locals import *
import Helpers
from Bound_Detector import Bound_Detector

"""
Player representation in game
"""
class Player(pygame.sprite.Sprite):
    reloadCounter = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Helpers.Assets.PLAYER)
        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (Helpers.GAME_WIDTH / 2, Helpers.GAME_HEIGHT / 2)
        self._speed = 5
        self._alive = True
        self._BULLETRELOAD = int(Helpers.FPS / 2)
    
    def update(self) -> list:
        if self._alive is False:
            return []

        pressedKeys = pygame.key.get_pressed()
        bullets = []

        # Movement
        if pressedKeys[K_w] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.UP):
            self.rect.move_ip(0, -self._speed)
        if pressedKeys[K_s] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.DOWN):
            self.rect.move_ip(0, self._speed)
        if pressedKeys[K_a] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.LEFT):
            self.rect.move_ip(-self._speed, 0)
        if pressedKeys[K_d] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.RIGHT):
            self.rect.move_ip(self._speed, 0)
        
        # Shooting
        if self._BULLETRELOAD == self.reloadCounter:
            if pressedKeys[K_UP]:
                bullets.append(Bullet(Helpers.Direction.UP, self.rect.center))
                self.reloadCounter = 0
            elif pressedKeys[K_DOWN]:
                bullets.append(Bullet(Helpers.Direction.DOWN, self.rect.center))
                self.reloadCounter = 0
            elif pressedKeys[K_LEFT]:
                bullets.append(Bullet(Helpers.Direction.LEFT, self.rect.center))
                self.reloadCounter = 0
            elif pressedKeys[K_RIGHT]:
                bullets.append(Bullet(Helpers.Direction.RIGHT, self.rect.center))
                self.reloadCounter = 0
        else:
            self.reloadCounter += 1

        return bullets
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def getCoords(self)-> tuple:
        if self._alive is False:
            return None
        return self.rect.center
    
    def killed(self):
        self._alive = False
        self.kill()

    def isAlive(self) -> bool:
        return self._alive

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction: "Direction", spawn: tuple):
        super().__init__()
        self.image = pygame.image.load(Helpers.Assets.BULLET)
        self._dir = direction
        self.rect = pygame.Surface((self.image.get_width(), self.image.get_height())).get_rect()
        self._speed = 8
        self.rect = self.rect.move(spawn)

    def update(self):
        if not Bound_Detector.check(self.rect, self._speed, self._dir):
            self.kill()
            
        if self._dir == Helpers.Direction.UP:
            self.rect.move_ip(0, -self._speed)
        elif self._dir == Helpers.Direction.RIGHT:
            self.rect.move_ip(self._speed, 0)
        elif self._dir == Helpers.Direction.DOWN:
            self.rect.move_ip(0, self._speed)
        elif self._dir == Helpers.Direction.LEFT:
            self.rect.move_ip(-self._speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)