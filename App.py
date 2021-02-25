import pygame
import random
from pygame.locals import *
import Helpers
from Player import Player
from Enemy import Enemy
from Clock import Clock
from Bound_Detector import Bound_Detector
from Background import Background
from Opening import Opening

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._enemyTimer = 0
        self._ENEMYSPAWNTIME = Helpers.FPS * 2
        self._player = Player()
        self._entities = pygame.sprite.Group()
        self._entities.add(self._player)
        self._mobs = pygame.sprite.Group()
        self._bullets = pygame.sprite.Group()
        self._background = Background()
        self._clock = None
        self._paused = False
        self._opening = Opening()
 
    def on_init(self):
        pygame.init()
        self._clock = Clock(pygame.font)
        self._display_surf = pygame.display.set_mode(Helpers.GAME_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        pygame.display.set_caption("Life in the Valley")
        
 
    def on_event(self, event):
        print("Event: ", event.type)

        if not self._opening.isAlive() and event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                self._paused = not self._paused
                
            if event.key == K_r:
                self.__init__()
                self._clock = Clock(pygame.font)
                self._display_surf = pygame.display.set_mode(Helpers.GAME_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)

        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            self._opening.startGame(mouse)

    def on_loop(self):
        if self._opening.isAlive():
            return

        if self._player.isAlive() and self._enemyTimer == self._ENEMYSPAWNTIME:
            toSpawn = Enemy.spawnEnemy(self._clock.getRound() + 1)
            for mob in toSpawn:
                self._entities.add(mob)
                self._mobs.add(mob)
            self._enemyTimer = 0
        else:
            self._enemyTimer += 1

        mob = pygame.sprite.spritecollideany(self._player, self._mobs)
        if mob:
            self._player.killed()
            self._clock.kill()
            self._paused = True
        pygame.sprite.groupcollide(self._bullets, self._mobs, True, True)

        self._clock.incrTime()

    def on_render(self):
        if self._opening.isAlive():
            self._opening.draw(self._display_surf)
            pygame.display.update()
            return

        self._display_surf.fill(Helpers.Colours.BLANK)
        self._background.draw(self._display_surf)
        for entity in self._entities:
            entity.draw(self._display_surf)
        self._clock.render(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while (self._running):
            
            if not self._paused:
                for event in pygame.event.get():
                    self.on_event(event)

                shots = self._player.update()

                for shot in shots:
                    self._bullets.add(shot)
                    self._entities.add(shot)
                
                for mob in self._mobs:
                    mob.update(self._player.getCoords())
                
                for bullet in self._bullets:
                    bullet.update()

                self.on_loop()

                self.on_render()
            else:
                for event in pygame.event.get():
                    self.on_event(event)


            pygame.time.Clock().tick(Helpers.FPS)

        self.on_cleanup()



if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
