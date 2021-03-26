from math import sqrt
from Vec import Vector
from time import time as t

class Entity:

    def __init__(self, pos, game,size):
        self.pos = [pos[0]*64 + 32,pos[1]*64 + 32]
        self.game = game
        self.size = size #actually half the size of the hitbox!!
        self.grounded = False
        self.vel = Vector(0,0)
        self.acc = Vector(0,0)
    
    def applyF(self):
        self.vel += self.acc
        self.acc = Vector(0,0)
    
    def fricNgrav(self): #friction and gravity
        if self.grounded: #horizontal friction, proportional to speed
            rxvel = self.vel.x / 5 #reduced X vel, reducing the constant raises the friction.
            self.acc -= (Vector(rxvel,0))
        else:
            rxvel = self.vel.x / 20
            self.acc -= (Vector(rxvel,0))

        if (not self.grounded):
            self.acc += Vector(0,1.5) #grav

    def col(self):
        if self.grounded:
            self.vel.y = 0

        self.grounded = False
        solid = [1] #define solid blocks
        loc = [int(self.pos[0] // 64), int(self.pos[1] // 64)]
        for i in range(-1,2): #Not well secured, but the player shouldn't be on the edge of the map anyway
            for j in range(-1,2): #goes around the player
                if self.game.level.level_array[loc[1]+j][loc[0]+i] in solid: #if the pointed block is solid
                    posb = (loc[0]+i)*64, (loc[1]+j)*64
                    if posb[1] - self.size < self.pos[1] < posb[1] + 64 + self.size : #Look at the paint
                        if (self.pos[0] < posb[0]) and (self.pos[0] + self.size + self.vel.x > posb[0]): #if on the left AND the speed will make it go through
                            self.pos[0] = posb[0] - self.size
                            self.vel.x = 0
                        elif (self.pos[0] > posb[0]) and (self.pos[0] - self.size + self.vel.x < posb[0]+64): # on the right
                            self.pos[0] = posb[0] + 64 + self.size
                            self.vel.x = 0

                    if posb[0] - self.size < self.pos[0] < posb[0] + 64 + self.size :
                        if (not self.grounded) and (self.pos[1] < posb[1]) and (self.pos[1] + self.size + self.vel.y + 0.001 > posb[1]): #the 0.001 makes sure we are looking inside of the block if 
                            self.pos[1] = posb[1] - self.size
                            self.vel.y = 0
                            self.grounded = True

                        elif (self.pos[1] > posb[1]) and (self.pos[1] - self.size + self.vel.y < posb[1]+64): 
                            self.pos[1] = posb[1] + 64 + self.size
                            self.vel.y = 0
    def nullify(self):
        if abs(self.vel.x) < 0.05:
            self.vel.x = 0
        if abs(self.vel.y) < 0.05:
            self.vel.y = 0
    def update(self):
        self.pos = list(self.vel.cast(self.pos))
        self.nullify()
        