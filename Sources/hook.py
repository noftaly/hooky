import pygame as pg
from Vector import Vector
from entity import Entity

class Hook(Entity):
    LAUNCH_SPEED = 50
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
            if self.impact:
                self.dest = self.pos
                self.gripped = True
            super().update()

            self.length = (self.pos - self.player.pos).mag()
            if not self.gripped and self.length > Hook.MAX_SIZE:
                self.reset()

    def collision(self):
        self.impact = False
        solid = [1,2,3] # Define solid blocks
        loc = self.pos // 64
        loc.with_ints()
        # Not well secured, but the player shouldn't be on the edge of the map anyway
        for i in range(-1, 2):
            # Goes around the player
            for j in range(-1, 2):
                # If the pointed block is solid
                if self.game.level.level_array[loc.y+j][loc.x+i] in solid:
                    neighbor = Vector((loc.x+i)*64, (loc.y+j)*64)
                    # Look at /collisions.png
                    if neighbor.y - self.size < self.pos.y < neighbor.y + 64 + self.size:
                        # If on the left AND the speed will make it go through
                        if (self.pos.x < neighbor.x) and (self.pos.x + self.size + self.vel.x > neighbor.x):
                            self.pos.x = neighbor.x - self.size
                            self.vel.x = 0
                            self.impact = True
                        # On the right
                        elif (self.pos.x > neighbor.x) and (self.pos.x - self.size + self.vel.x < neighbor.x+64):
                            self.pos.x = neighbor.x + 64 + self.size
                            self.vel.x = 0
                            self.impact = True

                    if neighbor.x - self.size < self.pos.x < neighbor.x + 64 + self.size :
                        # The 0.001 makes sure we are looking inside of the block if 
                        if (not self.grounded) and (self.pos.y < neighbor.y) and (self.pos.y + self.size + self.vel.y + 0.001 > neighbor.y):
                            self.pos.y = neighbor.y - self.size
                            self.vel.y = 0
                            self.impact = True

                        elif (self.pos.y > neighbor.y) and (self.pos.y - self.size + self.vel.y < neighbor.y+64): 
                            self.pos.y = neighbor.y + 64 + self.size
                            self.vel.y = 0
                            self.impact = True