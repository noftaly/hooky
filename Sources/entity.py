from vector import Vector

class Entity:
    FRICTION = 5
    GRAVITY = 0.3

    def __init__(self, cell, game,size):
        self.pos = Vector(cell.x * 64 + 32, cell.y * 64 + 32)
        self.cell = cell
        self.game = game
        self.size = size # Actually half the size of the hitbox!!
        self.grounded = False
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    def add_friction(self):
        if self.grounded: # Horizontal friction, proportional to speed
            # Reduce the X vel, reducing the constant raises the friction.
            self.acc -= Vector(self.vel.x / Entity.FRICTION, 0)
        else:
            self.acc -= Vector(self.vel.x / (Entity.FRICTION * 4), 0)

    def add_gravity(self):
        if not self.grounded:
            self.acc += Vector(0, Entity.GRAVITY)


    def nullify(self):
        """ When vel approaches 0, set it to 0, because otherwise there are cases where it will
        never reach 0 and we will always have a base velocity. """
        if abs(self.vel.x) < 0.05:
            self.vel.x = 0
        if abs(self.vel.y) < 0.05:
            self.vel.y = 0

    def update(self):
        self.pos += self.vel
        self.nullify()
        self.cell = (self.pos - 32) // 64
