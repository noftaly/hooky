from math import sqrt
from utils import get_2d_array
from vector import Vector

class Entity:
    GRAVITY = Vector(0, 0.2)

    def __init__(self, location, mass):
        self.pos = Vector(location.x * 64 + 32, location.y * 64 + 32)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass
        self.radius = sqrt(self.mass) * 10

    def friction(self):
        # Should check if it is in contact with a surface
        if True:
            # Shortcut:
            # self.acc *= 0.95

            # Compute the friction
            friction = self.vel.normalize() * -1 # Compute the direction (opposite to velocity)
            friction = friction.normalize()      # Normalize the direction
            friction *= 0.1 # Compute the magnitude

            # Apply friction
            self.apply_force(friction)

    def gravity(self):
        # Compute the weight based on the mass and gravity
        gravity = Entity.GRAVITY
        self.apply_force(gravity)

    def apply_force(self, force):
        self.acc += force

    def edges(self, level_array):
    	# Whenever it hits an edge, we invert its velocity (*-1), but we also
    	# reduce it a bit, because of the energy transfer.
        current_cell = round(Vector((self.pos.x - 32) / 64, (self.pos.y - 32) / 64))

        block_left = get_2d_array(level_array, current_cell.x - 1, current_cell.y)
        block_right = get_2d_array(level_array, current_cell.x + 1, current_cell.y)
        # block_above = get_2d_array(level_array, current_cell.x, current_cell.y - 1)
        # block_below = get_2d_array(level_array, current_cell.x, current_cell.y + 1)

        # Check at left
        if block_left == 1 and self.pos.x - 32 < current_cell.x * 64:
            self.pos.x = current_cell.x * 64 + self.radius * 2 + 1
            self.vel.x *= -0.4
        # Check at right
        if block_right == 1 and self.pos.x - 32 > current_cell.x * 64:
            self.pos.x = current_cell.x * 64 + self.radius * 2 - 1
            self.vel.x *= -0.4

    def update(self):
        # Add the acceleration to the velocity, and add the velocity to the position.
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0, 0)

        # Avoid weird bug where the velocity will approaches 0 without ever getting to it...
        if -1 < self.vel.x < 1:
            self.vel.x = 0
