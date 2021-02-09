import pygame
import random
from pygame.locals import *
import Helpers
from Player import Player
from Enemy import Enemy
from Bound_Detector import Bound_Detector
from Background import Background

class App:
    size = width, height = Helpers.GAME_SIZE
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._FPS = 30
        self._enemyTimer = 0
        self._ENEMYSPAWNTIME = self._FPS * 2
        self._player = Player()
        self._entities = pygame.sprite.Group()
        self._entities.add(self._player)
        self._mobs = pygame.sprite.Group()
        self._background = Background()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        pygame.display.set_caption("Life in the Valley")
        
 
    def on_event(self, event):
        print("Event: ", event.type)

        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        return
        if self._enemyTimer == self._ENEMYSPAWNTIME:
            enemy = Enemy()
            self._entities.add(enemy)
            self._mobs.add(enemy)
            self._enemyTimer = 0
        else:
            self._enemyTimer += 1

        mob = pygame.sprite.spritecollideany(self._player, self._mobs)
        if mob:
            mob.kill()


    def on_render(self):
        self._display_surf.fill(Helpers.Colours.BLANK)
        self._background.draw(self._display_surf)
        for entity in self._entities:
            entity.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while (self._running):

            for event in pygame.event.get():
                self.on_event(event)

            for entity in self._entities:
                entity.update()

            self.on_loop()

            self.on_render()

            pygame.time.Clock().tick(self._FPS)

        self.on_cleanup()



if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()