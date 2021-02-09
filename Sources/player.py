import pygame as pg

from vector import Vector

class Player:
    def __init__(self, game, spn):
        self.game = game
        self.pos = Vector(spn[0]*64 + 32, spn[1]*64 + 32)
        # Acceleration vector (x, y)
        self.acc = Vector(0, 0)

    def display(self):
        pg.draw.circle(self.game.surf, (0, 0, 255), self.game.hsize, 26)

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
