from math import sqrt
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

    def edges(self):
    	# Whenever it hits an edge, we invert its velocity (*-1), but we also
    	# reduce it a bit, because of the energy transfer.
        # TODO
        pass

    def update(self):
        # Add the acceleration to the velocity, and add the velocity to the position.
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0, 0)

        # Avoid weird bug where the velocity will approaches 0 without ever getting to it...
        if -1 < self.vel.x < 1:
            self.vel.x = 0
