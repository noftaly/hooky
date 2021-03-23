import pygame as pg
from entity import Entity
from Vec import Vector

class Player(Entity):
    def __init__(self, game, spawn_location):
        super().__init__(spawn_location, game,26)

    def display(self):
        pg.draw.circle(self.game.surface, (0, 0, 255), self.game.half_size, int(self.size*1.2)) #bit bigger than the hitbox to make it look cuul

    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[self.game.lft_k]:
            self.acc += Vector(-0.01, 0)
        if keys[self.game.rgt_k]:
            self.acc += Vector(0.01, 0)
        if keys[self.game.up_k] and self.grounded:
            self.acc += Vector(0, -1)
            self.grounded = False
    def update(self):
        #applie forces
        super().fricNgrav()
        self.handle_input()


        #takes them into account
        super().update()
