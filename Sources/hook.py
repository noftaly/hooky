import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    def __init__(self, player, game):
        super().__init__(player.cell, game, 5)

        self.player = player
        self.visible = False
        self.direction = Vector(0, 0)
        self.vel = Vector(3, 0)

    def reset(self):
        self.pos = self.player.pos
        self.cell = (self.pos - 32) // 64
        self.direction = Vector(0, 0)
        self.visible = False

    def display(self):
        position = (
                    self.game.half_size[0] - (self.pos.x - self.player.pos.x),
                    self.game.half_size[1] - (self.pos.y - self.player.pos.y)
                    )
        pg.draw.circle(self.game.surface, (0, 0, 0), position, int(self.size))

