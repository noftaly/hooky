import pygame as pg

from level import Level
from vector import Vector
from player import Player


class Game:
    def __init__(self, number_level):
        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.hsize = self.size[0] / 2, self.size[1] / 2

        self.level = Level(self, number_level)
        self.player = Player(self, self.level.spawn)
        self.running = True

    def handleEvent(self,event): #changes proprieties in function of the input
        if event.type == pg.QUIT:
            self.running = False

    def display(self):
        self.surface.fill((0,0,0))
        self.level.display()
        self.player.display()

        pg.display.update()

    #AUCUN OBJET PG DANS UPDATE !!!
    def update(self): #next tick (ajout de toute les accélérations aux vitesses et ajout de toute les vitesses aux positions)
        self.player.update_pos()
        self.player.apply_momentum()

    def main(self):
        i = 0
        while self.running:
            self.display()
            self.update()
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.player.acc += Vector(-2, 0)
            elif keys[pg.K_RIGHT]:
                self.player.acc += Vector(2, 0)
            for event in pg.event.get():
                self.handleEvent(event)
            pg.event.clear()

            i += 5
