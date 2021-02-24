import Helpers
import pygame

class Button:
    def __init__(self, assetPath):
        self._image = pygame.image.load(assetPath)
        self._surface = pygame.Surface((self._image.get_width(), self._image.get_height()))
        self._rect = self._surface.get_rect()
        self._width, self._height = self._image.get_width(), self._image.get_height()
    
    def draw(self, surface):
        surface.blit(self._image, self._rect)

    def getSize(self) -> tuple:
        return (self._width, self._height)

    def pressed(self):
        pass