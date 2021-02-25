import Helpers
import pygame

class Button:
    def __init__(self, assetPath: str, coords: tuple):
        self._image = pygame.image.load(assetPath)
        self._surface = pygame.Surface((self._image.get_width(), self._image.get_height()))
        self._rect = self._surface.get_rect()
        self._rect.topleft = coords
        self._width, self._height = self._image.get_width(), self._image.get_height()
    
    def draw(self, surface):
        surface.blit(self._image, self._rect)

    def getSize(self) -> tuple:
        return (self._width, self._height)

    def checkPressed(self, mouse: tuple) -> bool:
        mouseX, mouseY = mouse
        if self._rect.left <= mouseX and self._rect.right >= mouseX:
            if self._rect.top <= mouseY and self._rect.bottom >= mouseY:
                return True
        return False

    def pressed(self):
        pass