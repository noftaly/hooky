import pygame as pg
from entity import Entity
from Vector import Vector
from hook import Hook

class Player(Entity):
    def __init__(self, game, spawn_location):
        super().__init__(spawn_location, game, 26)
        self.hook = Hook(self, game)

    def display(self):
        # Bit bigger than the hitbox to make it look cuul
        pg.draw.circle(self.game.surface, (0, 0, 255), self.game.half_size, int(self.size * 1.2))

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
            self.acc += Vector(0, -20)
            self.grounded = False

    def launch_hook(self, event_position):
        self.hook.visible = True
        self.hook.offset = self.pos

        position = Vector(
                    event_position[0] - self.game.half_size[0],
                    event_position[1] - self.game.half_size[1]
                    ) 
        self.hook.vel = position.normalize(1 * Hook.LAUNCH_SPEED)

    def stop_hook(self):
        self.hook.reset()

    def update(self):
        # Apply forces
        self.add_friction()
        self.add_gravity()
        self.handle_input()
        self.apply_forces()
        self.collision()

        # Takes them into account
        super().update()
