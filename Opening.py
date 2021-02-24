import pygame
import Helpers

class Opening:

    def __init__(self):
        self._screenCard = pygame.image.load(Helpers.Assets.OPENING_CARD)
        self._surfaceCard = pygame.Surface((self._screenCard.get_width(), self._screenCard.get_height()))
        self._rectCard = self._surface.get_rect()

        self._playBtn = pygame.image.load(Helpers.Assets.PLAY_BTN)
        self._playBtnSurface = pygame.Surface((self._playBtn.get_width(), self._playBtn.get_height()))
        self._playBtnRect = self._playBtnSurface.get_rect()

        self._alive = True

    def draw(self, surface):
        pass

    def close(self):
        self._alive = False

    def isAlive(self) -> bool:
        return self._alive