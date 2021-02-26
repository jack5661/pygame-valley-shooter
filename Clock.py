import Helpers
import pygame

"""
Keeps track of time in the game
"""
class Clock:
    ROUND_1 = 30
    ROUND_2 = 60
    ROUND_3 = 90
    ROUND = 15
    ROUND_COORD = (0, 0)
    TIMER_COORD = (Helpers.GAME_TILE * 12, 0)

    def __init__(self, fonts):
        self._round = 1
        self._font = fonts.SysFont("comicsansms", 30)
        self._roundMsg = self._font.render("Round 1", True, Helpers.Colours.BLACK)
        self._time = 0
        self._timeMsg = self._font.render("0", True, Helpers.Colours.BLACK)
        self._frameCounter = 0
        self._alive = True

    def getTime(self) -> int:
        return self._time
    
    def getRound(self) -> int:
        return self._round

    def kill(self):
        self._alive = False

    def incrTime(self) -> None:
        if self._alive is False:
            return

        self._frameCounter += 1
        if self._frameCounter == Helpers.FPS:
            self._time += 1
            self._timeMsg = self._font.render(str(self._time), self.TIMER_COORD, Helpers.Colours.BLACK)
            self._frameCounter = 0
            if self._time % self.ROUND == 0:
                self._round += 1
                self._roundMsg = self._font.render("Round " + str(self._round), self.ROUND_COORD, Helpers.Colours.BLACK)


    def render(self, surface: pygame.Surface):
        surface.blit(self._roundMsg, self.ROUND_COORD)
        surface.blit(self._timeMsg, self.TIMER_COORD)
        
        