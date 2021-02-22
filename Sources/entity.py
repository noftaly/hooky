from math import sqrt
from utils import get_2d_array, BlockDirection
from vector import Vector

class Entity:
    GRAVITY = Vector(0, 0.5)

    def __init__(self, location, mass, game):
        self.pos = Vector(location.x * 64 + 32, location.y * 64 + 32)
        self.cell = Vector(0, 0)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass
        self.radius = sqrt(self.mass) * 10
        self.game = game

    def friction(self):
        # TODO: Should check if it is in contact with a surface
        if True:
            # Shortcut:
            # self.acc *= 0.95

            # Compute the friction
            friction = self.vel.normalize() * -1 # Compute the direction (opposite to velocity)
            friction = friction.normalize()      # Normalize the direction
            friction *= 0.2 # Compute the magnitude

            # Apply friction
            self.apply_force(friction)

    def gravity(self):
        # Compute the weight based on the mass and gravity
        self.apply_force(Entity.GRAVITY)

    def apply_force(self, force):
        self.acc += force

    def has_block(self, direction):
        block = 0
        if direction == BlockDirection.ABOVE:
            block = get_2d_array(self.game.level.level_array, self.cell.x, self.cell.y - 1)
        elif direction == BlockDirection.BELOW:
            block = get_2d_array(self.game.level.level_array, self.cell.x, self.cell.y + 1)
        elif direction == BlockDirection.LEFT:
            block = get_2d_array(self.game.level.level_array, self.cell.x - 1, self.cell.y)
        elif direction == BlockDirection.RIGHT:
            block = get_2d_array(self.game.level.level_array, self.cell.x + 1, self.cell.y)
        return block == 1

    def intersects_with_neighbor(self, direction):
        if direction == BlockDirection.ABOVE:
            return self.pos.y - 32 < self.cell.y * 64
        if direction == BlockDirection.BELOW:
            return self.pos.y + 32 > (self.cell.y + 1) * 64
        if direction == BlockDirection.LEFT:
            return self.pos.x - 32 < self.cell.x * 64
        if direction == BlockDirection.RIGHT:
            return self.pos.x + 32 > (self.cell.x + 1) * 64

    def edges(self):
    	# Whenever it hits an edge, we invert its velocity (*-1), but we also
    	# reduce it a bit, because of the energy transfer.

        # Check at left
        if self.has_block(BlockDirection.LEFT) and self.intersects_with_neighbor(BlockDirection.LEFT):
            self.pos.x = self.cell.x * 64 + self.radius * 2 + 1
            self.vel.x *= -0.4
        # Check at right
        if self.has_block(BlockDirection.RIGHT) and self.intersects_with_neighbor(BlockDirection.RIGHT):
            self.pos.x = self.cell.x * 64 + self.radius * 2 - 1
            self.vel.x *= -0.4

        # Check above
        if self.has_block(BlockDirection.ABOVE) and self.intersects_with_neighbor(BlockDirection.ABOVE):
            self.pos.y = self.cell.y * 64 + self.radius * 2
            self.vel.y *= -0.4
        # Check below
        if self.has_block(BlockDirection.BELOW) and self.intersects_with_neighbor(BlockDirection.BELOW):
            self.pos.y = self.cell.y * 64 + self.radius * 2
            self.vel.y *= -0.4

    def update(self):
        # Add the acceleration to the velocity, and add the velocity to the position.
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0, 0)

        self.cell = round(Vector((self.pos.x - 32) / 64, (self.pos.y - 32) / 64))

        # Avoid weird bug where the velocity will approaches 0 without ever getting to it...
        if -0.1 < self.vel.x < 0.1:
            self.vel.x = 0
        if -0.1 < self.vel.y < 0.1:
            self.vel.y = 0
