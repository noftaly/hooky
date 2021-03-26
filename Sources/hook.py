import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    def __init__(self, player, game):
        super().__init__(player.cell, game, 5)

        self.player = player
        self.visible = False
        self.offset = Vector(0, 0)
        self.vel = Vector(0, 0)

    def reset(self):
        self.pos = self.player.pos
        self.cell = (self.pos - 32) // 64
        self.vel = Vector(0, 0)
        self.visible = False

    def display(self):
        position = (
                    self.game.half_size[0] - (self.offset.x - self.pos.x),
                    self.game.half_size[1] - (self.offset.y - self.pos.y)
                    )
        pg.draw.circle(self.game.surface, (0, 0, 0), position, int(self.size))

