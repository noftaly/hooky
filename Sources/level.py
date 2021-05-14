import random
import pygame as pg
from Vector import Vector

class Level:
    def __init__(self, game, number_level):
        self.number_level, self.game = number_level, game
        self.blocks_im = []
        self.spawn = Vector(0, 0)
        self.read_level(number_level)
        
        self.load_blocs()
        self.mk_lvl_surf()

    def load_blocs(self):
        self.blocks_im = []
        # Définir quel map a quel thème plus tard
        if 0 <= self.number_level <= 99:
            # À modifier quand on aura les assets par un for
            """b = pg.Surface((64, 64))
            b.fill((216, 106, 0))
            self.blocks_im.append(b)

            b = pg.Surface((64,64))
            b.fill((137,90,00))
            self.blocks_im.append(b)"""

            b = pg.image.load("./Assets/dirt_2.png")
            b = b_var = pg.transform.scale(b,(64,64))
            for i in range(3):
                b_var = pg.transform.rotate(b_var,-90)
                self.blocks_im.append(b_var)
            self.blocks_im.append(b)

    def mk_lvl_surf(self):
        """ Makes a pg Surface, that will be displayed over the background by Game """
        px_size = (len(self.level_array[0])*64, len(self.level_array)*64)
        red = pg.Surface((64,64))
        red.fill((255,0,0))

        self.lvl_surf = pg.Surface(px_size)
        # Tells pg that every perfectly black pixel should be transparent, the hex of black pixels should be 010101
        self.lvl_surf.set_colorkey((0, 0, 0))

        for x in range(len(self.level_array[0])):
            for y in range(len(self.level_array)):
                if self.level_array[y][x] == 1:
                    self.lvl_surf.blit(random.choice(self.blocks_im),(x*64,y*64))
                elif self.level_array[y][x] == 2:
                    self.lvl_surf.blit(red,(x*64,y*64))

    def display(self): 
        self.game.surface.blit(
            self.lvl_surf,
            (
                self.game.half_size[0] - self.game.player.pos.x,
                self.game.half_size[1] - self.game.player.pos.y
            )
        )

    def read_level(self, number_level):
        self.level_array = []
        # r+t: read as text file
        with open("./Levels/level_" + str(number_level) + ".lvl", mode='r+t') as level_file:
            for (row, line) in enumerate(level_file):
                if line[-1] == '\n':
                    line = line[:-1]
                if row == 0:
                    # Transforms a string "x,y" into a tuple (x,y), with x,y int, and then into a vector
                    spawn = tuple(map(int, line.split(',')))
                    self.spawn = Vector.from_tuple(spawn)
                else:
                    self.level_array.append(list(map(int, line)))
