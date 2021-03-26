from Vector import Vector

class Entity:
    FRICTION = 5
    GRAVITY = 1.5

    def __init__(self, pos, game,size):
        self.pos = Vector(pos.x * 64 + 32, pos.y * 64 + 32)
        self.game = game
        self.size = size # Actually half the size of the hitbox!!
        self.grounded = False
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
    
    def applyF(self):
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
                    posb = Vector((loc.x+i)*64, (loc.y+j)*64)
                    # Look at the paint
                    if posb.y - self.size < self.pos.y < posb.y + 64 + self.size :
                        # If on the left AND the speed will make it go through
                        if (self.pos.x < posb.x) and (self.pos.x + self.size + self.vel.x > posb.x):
                            self.pos.x = posb.x - self.size
                            self.vel.x = 0
                        # On the right
                        elif (self.pos.x > posb.x) and (self.pos.x - self.size + self.vel.x < posb.x+64):
                            self.pos.x = posb.x + 64 + self.size
                            self.vel.x = 0

                    if posb.x - self.size < self.pos.x < posb.x + 64 + self.size :
                        # The 0.001 makes sure we are looking inside of the block if 
                        if (not self.grounded) and (self.pos.y < posb.y) and (self.pos.y + self.size + self.vel.y + 0.001 > posb.y):
                            self.pos.y = posb.y - self.size
                            self.vel.y = 0
                            self.grounded = True

                        elif (self.pos.y > posb.y) and (self.pos.y - self.size + self.vel.y < posb.y+64): 
                            self.pos.y = posb.y + 64 + self.size
                            self.vel.y = 0
    def nullify(self):
        """ When vel approaches 0, set it to 0, because otherwise there are cases where it will
        never reach 0 and we will always have a base velocity. """
        if abs(self.vel.x) < 0.05:
            self.vel.x = 0
        if abs(self.vel.y) < 0.05:
            self.vel.y = 0

    def update(self):
        self.pos = self.vel.cast(self.pos)
        self.nullify()
        