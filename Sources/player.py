import pygame as pg

from vector import Vector

class Player:
    def __init__(self, game, spawn_location):
        self.game = game
        self.pos = Vector(spawn_location.x*64 + 32, spawn_location.y*64 + 32)
        self.acc = Vector(0, 0)

    def display(self):
        pg.draw.circle(self.game.surface, (0, 0, 255), self.game.hsize, 26)

    def update_pos(self):
        self.pos += self.acc

    def apply_momentum(self):
        # Update x
        if self.acc.x < 0:
            self.acc += Vector(1, 0)
        elif self.acc.x > 0:
            self.acc += Vector(-1, 0)
        # Update y
        if self.acc.x < 0:
            self.acc += Vector(1, 0)
        elif self.acc.x > 0:
            self.acc += Vector(-1, 0)
