import pygame
import Helpers
from Background import Background

class Bound_Detector():

    @staticmethod
    def check(rect: pygame.Rect, speed: int, dir: Helpers.Direction) -> bool:
        if dir == Helpers.Direction.UP:
            tile = Background.checkTile(rect.left, rect.top - speed)    
        elif dir == Helpers.Direction.RIGHT:
            tile = Background.checkTile(rect.right + speed, rect.top)
        elif dir == Helpers.Direction.DOWN:
            tile = Background.checkTile(rect.left, rect.bottom + speed)
        elif dir == Helpers.Direction.LEFT:
            tile = Background.checkTile(rect.left - speed, rect.top)
            
        if tile == Background.ROCK:
            return False
        elif tile == Background.SPACE:
            return False
        else:
            return True