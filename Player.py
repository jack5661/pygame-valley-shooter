import pygame
from pygame.locals import *
import Helpers
from Bound_Detector import Bound_Detector

class Player(pygame.sprite.Sprite):
    reloadCounter = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Helpers.ASSETS + "player.png")
        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (Helpers.GAME_WIDTH / 2, Helpers.GAME_HEIGHT / 2)
        self._speed = 5
        self._alive = True
        self._BULLETRELOAD = Helpers.FPS
    
    def update(self) -> "Bullet":
        pressedKeys = pygame.key.get_pressed()
        bullets = []

        # Movement
        if pressedKeys[K_a] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.UP):
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
            if pressedKeys[K_DOWN]:
                bullets.append(Bullet(Helpers.Direction.DOWN, self.rect.center))
            if pressedKeys[K_LEFT]:
                bullets.append(Bullet(Helpers.Direction.LEFT, self.rect.center))
            if pressedKeys[K_RIGHT]:
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction: "Direction", spawn: tuple):
        super().__init__()
        self.image = pygame.image.load(Helpers.ASSETS + "bullet.png")
        self._dir = direction
        self.rect = pygame.Surface((self.image.get_width(), self.image.get_height())).get_rect()
        self._speed = 2
        self.rect = self.rect.move(spawn)

    def update(self):
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