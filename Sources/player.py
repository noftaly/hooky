from time import time
import pygame as pg
from entity import Entity
from vector import Vector
from hook import Hook
from utils import get_asset

class Player(Entity):
    def __init__(self, game, spawn_location):
        super().__init__(spawn_location, game, 26)
        self.spawn = spawn_location * 64
        self.hook = Hook(self, game)

        self.dead = False
        self.load_sprites()
        self.right = True
        self.last_u = time()

        self.update_sprite()


    def display(self):
        # Bit bigger than the hitbox to make it look cuul
        image = self.image if self.right else pg.transform.flip(self.image,True,False)
        self.game.surface.blit(image,(self.game.half_size[0]-30, self.game.half_size[1]-30))

    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[self.game.left_key]:
            if self.grounded:
                self.acc += Vector(-1.7, 0)
            else:
                self.acc += Vector(-0.425, 0)
        if keys[self.game.right_key]:
            if self.grounded:
                self.acc += Vector(1.7, 0)
            else:
                self.acc += Vector(0.425, 0)

        if keys[self.game.up_key] and self.grounded:
            self.acc += Vector(0, -12)
            self.grounded = False

    def finish_level(self):
        self.game.next_level()

    def die(self):
        self.vel = Vector(0,0)
        self.game.sounds.get('damage').play()
        self.pos = self.game.level.spawn * 64
        self.stop_hook()

    def launch_hook(self, event_position):
        self.hook.reset()
        self.hook.offset = self.pos

        position = Vector(
            event_position[0] - self.game.half_size[0],
            event_position[1] - self.game.half_size[1]
        )
        if position.y:
            self.grounded = False
        self.hook.vel = position.normalize(Hook.LAUNCH_SPEED)
        self.hook.visible = True

    def stop_hook(self):
        self.hook.reset()

    def apply_hook(self):
        # Every value in there is found "à tâton", don't ask questions you won't get answers
        hook_acc = Vector(0,0)
        hook_acc = self.hook.pos - self.pos

        if (self.acc.x < 0 and hook_acc.x > 0) or (self.acc.x > 0 and hook_acc.x < 0):
            hook_acc.x *= 0.8
        if hook_acc.y > 0:
            hook_acc.y *= 0.8

        length = abs(hook_acc)
        norm = (length/Hook.MAX_SIZE) * 2.5

        norm = min(norm, 0.75)

        hook_acc = hook_acc.normalize(norm)
        self.acc += hook_acc

    def collision(self):
        if self.grounded:
            self.grounded = False

        solid = [1, 2, 3] # Define solid blocks
        loc = self.pos // 64
        loc.with_ints()
        # Not well secured, but the player shouldn't be on the edge of the map anyway
        for i in range(-1, 2):
            # Goes around the player
            for j in range(-1, 2):
                try:
                    self.game.level.level_array[loc.y + j][loc.x + i]
                except IndexError:
                    continue
                # If the pointed block is solid
                if self.game.level.level_array[loc.y + j][loc.x + i] in solid:
                    danger = self.game.level.level_array[loc.y + j][loc.x + i] == 2
                    finish = self.game.level.level_array[loc.y + j][loc.x + i] == 3
                    neighbor = Vector((loc.x + i) * 64, (loc.y + j) * 64)

                    # Look at /collisions.png
                    if neighbor.y - self.size < self.pos.y < neighbor.y + 64 + self.size:
                        # If on the left AND the speed will make it go through
                        if (self.pos.x < neighbor.x) and (self.pos.x + self.size + self.vel.x > neighbor.x):
                            if danger:
                                self.dead = True
                            if finish:
                                self.finish_level()
                            self.pos.x = neighbor.x - self.size
                            self.vel.x = 0
                        # On the right
                        elif (self.pos.x > neighbor.x) and (self.pos.x - self.size + self.vel.x < neighbor.x+64):
                            if danger:
                                self.dead = True
                            if finish:
                                self.finish_level()
                            self.pos.x = neighbor.x + 64 + self.size
                            self.vel.x = 0

                    if neighbor.x - self.size < self.pos.x < neighbor.x + 64 + self.size :
                        # The 0.001 makes sure we are looking inside of the block if
                        if (not self.grounded) and (self.pos.y < neighbor.y) and (self.pos.y + self.size + self.vel.y + 0.001 > neighbor.y):
                            if danger:
                                self.dead = True
                            if finish:
                                self.finish_level()
                            self.pos.y = neighbor.y - self.size
                            self.vel.y = 0
                            self.grounded = True

                        elif (self.pos.y > neighbor.y) and (self.pos.y - self.size + self.vel.y < neighbor.y+64):
                            if danger:
                                self.dead = True
                            if finish:
                                self.finish_level()
                            self.pos.y = neighbor.y + 64 + self.size
                            self.vel.y = 0

    def update(self):
        # Apply forces
        self.update_sprite()
        self.handle_input()

        if self.hook.visible and self.hook.gripped:
            self.apply_hook()

        self.add_friction()
        self.add_gravity()

        self.vel += self.acc
        norm = abs(self.vel)
        #allez savoir pourquoi ce tweak rends le grappin 10x plus agréable
        if self.hook.gripped:
            self.vel = self.vel.normalize(min(norm,11.5))
        else:
            self.vel.y = min(self.vel.y,12)
        #self.vel.y = min(self.vel.y, 15)
        self.collision()
        if self.dead:
            self.die()
            self.dead = False
        self.acc = Vector(0, 0)

        # Takes them into account
        super().update()

    def load_sprites(self):
        self.sprites = []
        for i in range(1,8):
            self.sprites.append(
                pg.image.load(get_asset(f"Images/hooky_{i}.png"))
            )
        for i in range(len(self.sprites)):
            self.sprites[i] = pg.transform.scale(self.sprites[i], (60, 60))
        self.sprite_index = 0

    def update_sprite(self):

        if self.vel.x == 0:
            self.image = self.sprites[2]
        else:
            if (self.vel.x > 0)^(self.right):
                self.right = not self.right

            if self.vel.y < -1 :
                self.image = self.sprites[5]
            elif self.vel.y > 1:
                self.image = self.sprites[6]
            else:
                if (self.vel.x > 0)^(self.right):
                    self.right = not self.right
                if time()-self.last_u > (1/24):
                    self.last_u = time()
                    if self.grounded:
                        self.sprite_index = (self.sprite_index + 1)%5

                self.image = self.sprites[self.sprite_index]
