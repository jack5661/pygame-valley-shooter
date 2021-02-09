import pygame
import Helpers
import math

class Background():
    ROCK = 0
    FLOOR = 1
    SPACE = 3
    _tileSet = None

    def __init__(self):
        self._floor = pygame.image.load(Helpers.ASSETS + "Floor.png")
        self._rock = pygame.image.load(Helpers.ASSETS + "Rock.png")
        self._surface = pygame.Surface((Helpers.GAME_TILE, Helpers.GAME_TILE))
        self._rect = self._surface.get_rect()
        self._tileDict = {self.ROCK: self._rock, self.FLOOR: self._floor}
        self.initTileSet()
    
    @classmethod
    def initTileSet(cls):
        sideRocks = [cls.ROCK] * 1 + [cls.FLOOR] * 11 + [cls.ROCK] * 1
        topBottom = [cls.ROCK] * 5 + [cls.FLOOR] * 3 + [cls.ROCK] * 5
        openRocks = [cls.FLOOR] * 13

        cls._tileSet = tuple(topBottom +
                         sideRocks * 2 +
                         openRocks * 2 +
                         sideRocks * 2 +
                         topBottom
                        )

    def draw(self, surface):
        for x in range(len(self._tileSet)):
            image = self._tileDict[self._tileSet[x]]
            surface.blit(image, self._rect)
            if (x + 1) % (Helpers.GAME_WIDTH / Helpers.GAME_TILE) != 0:
                self._rect.move_ip(Helpers.GAME_TILE, 0)
                wut = (x + 1) % (Helpers.GAME_WIDTH / Helpers.GAME_TILE)
            else:
                self._rect.move_ip(-Helpers.GAME_WIDTH + Helpers.GAME_TILE, Helpers.GAME_TILE)
        self._rect.move_ip((0, -Helpers.GAME_HEIGHT))
    
    @classmethod
    def checkTile(cls, x: int, y: int):
        if x < 0 or y < 0 or x > Helpers.GAME_WIDTH:
            return cls.SPACE
        yTile = int(y / Helpers.GAME_TILE)
        xTile = math.floor(x / Helpers.GAME_TILE)
        tileIdx = xTile + yTile * (Helpers.GAME_WIDTH / Helpers.GAME_TILE)
        try:
            if cls._tileSet[int(tileIdx)] == cls.ROCK:
                return cls.ROCK
            else:
                return cls.FLOOR
        except IndexError:
            return cls.SPACE


