import pygame as pg

from level import Level
from Vec import Vector
from player import Player
import time as t


class Game:
    CELL_SIZE = 64

    def __init__(self, number_level):
        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.half_size = self.size[0] // 2, self.size[1] // 2

        self.bckg = pg.Surface(self.size)
        self.bckg.fill((0,240,240))

        self.level = Level(self, number_level)
        self.player = Player(self, self.level.spawn)

        self.read_cfg()
        self.running = True

    def read_cfg(self): # à faire dans Menu plus tard
        self.up_k = pg.K_UP
        self.lft_k = pg.K_LEFT
        self.rgt_k = pg.K_RIGHT
    def handle_event(self,event): 
        if event.type == pg.QUIT:
            self.running = False

    def display(self):
        self.surface.blit(self.bckg,(0,0))
        
        self.level.display()
        self.player.display()

        pg.display.update()

    # NOTE: No PyGame object in update()!
    def update(self):
        """ Update entities """
        self.player.update()
        pass

    def main(self):
        while self.running:
            self.display()
            self.update()
            t.sleep(0.00833)
            for event in pg.event.get():
                self.handle_event(event)