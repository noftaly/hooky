import pygame as pg

from level import Level
from vector import Vector
from player import Player


class Game:
    CELL_SIZE = 64

    def __init__(self, number_level):
        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.half_size = self.size[0] / 2, self.size[1] / 2

        self.level = Level(self, number_level)
        self.player = Player(self, self.level.spawn)
        self.running = True

    def handleEvent(self,event):
        if event.type == pg.QUIT:
            self.running = False

    def display(self):
        self.surface.fill((0, 0, 0))
        self.level.display()
        self.player.display()

        pg.display.update()

    # NOTE: No PyGame object in update()!
    def update(self):
        """ Update entities """
        self.player.gravity()
        self.player.friction()
        self.player.edges()
        self.player.update()

    def main(self):
        while self.running:
            self.display()
            self.update()

            # We treat direction keys separately to allow keeping them pressed.
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.player.acc += Vector(-1, 0)
            elif keys[pg.K_RIGHT]:
                self.player.acc += Vector(1, 0)

            for event in pg.event.get():
                self.handleEvent(event)
            pg.event.clear()
