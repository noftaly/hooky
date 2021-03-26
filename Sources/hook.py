import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    def __init__(self, player, game):
        super().__init__(player.pos, game, 5)

        self.player = player
        self.visible = False
        self.direction = Vector(0, 0)
        self.vel = Vector(3, 0)

    def display(self):
        print(self.pos.as_tuple())
        exit(1)
        pg.draw.circle(self.game.surface, (0, 0, 0), self.pos.as_tuple(), int(self.size))
