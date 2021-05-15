import pygame as pg

from level import Level
from player import Player
import time as t

class Game:
    CELL_SIZE = 64

    def __init__(self, parent, number_level):
        self.parent = parent
        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.half_size = self.size[0] // 2, self.size[1] // 2

        self.background = pg.Surface(self.size)
        self.background.fill((0,240,240))

        self.level = Level(self, number_level)
        self.player = Player(self, self.level.spawn)

        self.config = self.parent.config
        self.up_key = self.config[2][2] # pg.K_UP
        self.left_key = self.config[2][0] # pg.K_LEFT
        self.right_key = self.config[2][1] # pg.K_RIGHT

        self.running = True 

    def handle_event(self, event): 
        if event.type == pg.QUIT:
            self.running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            self.player.launch_hook(event.pos)
        if event.type == pg.MOUSEBUTTONUP and event.button == 3:
            self.player.stop_hook()

    def display(self):
        """ Update the graphics """
        self.surface.blit(self.background, (0, 0))
        
        self.level.display()
        if self.player.hook.visible:
            self.player.hook.display()
        self.player.display()

        pg.display.update()

    # NOTE: No PyGame object in update()!
    def update(self):
        """ Update entities """
        self.player.update()
        if self.player.hook.visible:
            self.player.hook.update()

    def main(self):
        while self.running:
            st = t.time()
            self.display()
            self.update()
            for event in pg.event.get():
                self.handle_event(event)
            slp = 0.0083 - t.time() + st
            if slp>0:
                t.sleep(slp)
