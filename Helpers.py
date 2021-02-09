import pygame

ASSETS = "assets/"

GAME_SIZE = GAME_WIDTH, GAME_HEIGHT = 650, 400

GAME_TILE = 50

class Colours:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    BLANK = (0, 0, 0, 0)

class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

