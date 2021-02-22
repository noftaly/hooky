import pygame as pg
from entity import Entity

class Player(Entity):
    def __init__(self, game, spawn_location):
        super().__init__(spawn_location, 2.56, game)

    def display(self):
        pg.draw.circle(self.game.surface, (0, 0, 255), self.game.half_size, self.radius * 2)
