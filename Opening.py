import pygame
import Helpers
from Button import Button

class Opening:
    PLAYBTN_X = 250
    PLAYBTN_Y = 220
    TITLE_COORD = (200, 150)
    
    def __init__(self):
        self._screenCard = pygame.image.load(Helpers.Assets.OPENING_CARD)
        self._surfaceCard = pygame.Surface((self._screenCard.get_width(), self._screenCard.get_height()))
        self._rectCard = self._surfaceCard.get_rect()

        self._playBtn = Button(Helpers.Assets.PLAY_BTN, (self.PLAYBTN_X, self.PLAYBTN_Y))

        self._font = None
        self._title = None

        self._alive = True

    def draw(self, surface):
        surface.blit(self._screenCard, self._rectCard)
        surface.blit(self._title, self.TITLE_COORD)
        self._playBtn.draw(surface)

    def initTitle(self, fonts):
        if self._alive:
            self._font = fonts.SysFont("comicsansms", 40)
            self._title = self._font.render(Helpers.GAME_TITLE, True, Helpers.Colours.WHITE)

    def isAlive(self) -> bool:
        return self._alive

    def startGame(self, mouse: tuple) -> bool:
        if self._playBtn.checkPressed(mouse):
            self._alive = False
        else:
            return False