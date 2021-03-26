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
        # Bit bigger than the hitbox to make it look cuul
        pg.draw.circle(self.game.surface, (0, 0, 0), self.game.half_size, int(self.size))
