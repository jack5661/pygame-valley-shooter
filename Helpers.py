import pygame
import random

ASSETS = "assets/"

GAME_SIZE = GAME_WIDTH, GAME_HEIGHT = 650, 400

GAME_TILE = 50

FPS = 30

class Colours:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    BLANK = (0, 0, 0, 0)

class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @classmethod
    def rotateDirection(cls, dir: "Direction") -> "Direction":
        if dir == cls.UP:
            return cls.RIGHT
        elif dir == cls.RIGHT:
            return cls.DOWN
        elif dir == cls.DOWN:
             return cls.LEFT
        elif dir == cls.LEFT:
            return cls.UP
    
    @staticmethod
    def randomDirection():
        return random.randrange(0, 4)
        

