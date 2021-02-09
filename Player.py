import pygame
from pygame.locals import *
import Helpers
from Bound_Detector import Bound_Detector

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Helpers.ASSETS + "player.png")
        self.surface = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (Helpers.GAME_WIDTH / 2, Helpers.GAME_HEIGHT / 2)
        self._speed = 5
    
    def update(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_UP] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.UP):
            self.rect.move_ip(0, -self._speed)
        if pressedKeys[K_DOWN] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.DOWN):
            self.rect.move_ip(0, self._speed)
        if pressedKeys[K_LEFT] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.LEFT):
            self.rect.move_ip(-self._speed, 0)
        if pressedKeys[K_RIGHT] and Bound_Detector.check(self.rect, self._speed, Helpers.Direction.RIGHT):
            self.rect.move_ip(self._speed, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)