from Vector import Vector

class Entity:
    FRICTION = 5
    GRAVITY = 1.4

    def __init__(self, cell, game,size):
        self.pos = Vector(cell.x * 64 + 32, cell.y * 64 + 32)
        self.cell = cell
        self.game = game
        self.size = size # Actually half the size of the hitbox!!
        self.grounded = False
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
    
    def apply_forces(self):
        self.vel += self.acc
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

    def collision(self):
        if self.grounded:
            self.vel.y = 0
            self.grounded = False

        solid = [1] # Define solid blocks
        loc = self.pos // 64
        loc.with_ints()
        # Not well secured, but the player shouldn't be on the edge of the map anyway
        for i in range(-1,2):
            # Goes around the player
            for j in range(-1,2):
                # If the pointed block is solid
                if self.game.level.level_array[loc.y+j][loc.x+i] in solid:
                    neighbor = Vector((loc.x+i)*64, (loc.y+j)*64)
                    # Look at /collisions.png
                    if neighbor.y - self.size < self.pos.y < neighbor.y + 64 + self.size:
                        # If on the left AND the speed will make it go through
                        if (self.pos.x < neighbor.x) and (self.pos.x + self.size + self.vel.x > neighbor.x):
                            self.pos.x = neighbor.x - self.size
                            self.vel.x = 0
                        # On the right
                        elif (self.pos.x > neighbor.x) and (self.pos.x - self.size + self.vel.x < neighbor.x+64):
                            self.pos.x = neighbor.x + 64 + self.size
                            self.vel.x = 0

                    if neighbor.x - self.size < self.pos.x < neighbor.x + 64 + self.size :
                        # The 0.001 makes sure we are looking inside of the block if 
                        if (not self.grounded) and (self.pos.y < neighbor.y) and (self.pos.y + self.size + self.vel.y + 0.001 > neighbor.y):
                            self.pos.y = neighbor.y - self.size
                            self.vel.y = 0
                            self.grounded = True

                        elif (self.pos.y > neighbor.y) and (self.pos.y - self.size + self.vel.y < neighbor.y+64): 
                            self.pos.y = neighbor.y + 64 + self.size
                            self.vel.y = 0

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
