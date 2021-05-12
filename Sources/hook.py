import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    LAUNCH_SPEED = 30
    MAX_SIZE = 64 * 8

    def __init__(self, player, game):
        super().__init__(player.cell, game, 1)

        self.player = player
        self.visible = False
        self.gripped = False
        self.vel = Vector(0, 0)
        self.length = 0

    def reset(self):
        self.pos = self.player.pos
        self.cell = (self.pos - 32) // 64
        self.vel = Vector(0, 0)
        self.visible = False
        self.gripped = False

    def display(self):
        halfsize = Vector.from_tuple(self.game.half_size)
        position = halfsize - self.player.pos + self.pos

        pg.draw.line(self.game.surface, (0, 0, 0), self.game.half_size, position.as_tuple(), 3)
        pg.draw.circle(self.game.surface, (0, 0, 0), position.as_tuple(), self.size * 5)

    def update(self):
        if not self.gripped:
            self.collision()
            # If we hit something
            if self.vel.x == 0 or self.vel.y == 0:
                self.dest = self.pos
                self.gripped = True
            super().update()

            self.length = (self.pos - self.player.pos).mag()
            if not self.gripped and self.length > Hook.MAX_SIZE:
                self.reset()
