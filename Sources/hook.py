import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    LAUNCH_SPEED = 30

    def __init__(self, player, game):
        super().__init__(player.cell, game, 5)

        self.player = player
        self.visible = False
        self.stopped = False
        self.offset = Vector(0, 0)
        self.vel = Vector(0, 0)

    def reset(self):
        self.pos = self.player.pos
        self.cell = (self.pos - 32) // 64
        self.vel = Vector(0, 0)
        self.visible = False
        self.stopped = False

    def display(self):
        position = (
                    self.game.half_size[0] - (self.offset.x - self.pos.x),
                    self.game.half_size[1] - (self.offset.y - self.pos.y)
                    )

        pg.draw.line(self.game.surface, (0, 0, 0), self.game.half_size, position, 3)
        pg.draw.circle(self.game.surface, (0, 0, 0), position, int(self.size))

    def update(self):
        if not self.stopped:
            self.collision()
            # If we hit something
            if self.vel.x == 0 or self.vel.y == 0:
                self.dest = self.pos
                self.stopped = True
            super().update()
