import random
from datetime import datetime
import pygame as pg
from utils import get_asset
from vector import Vector

class Level:
    def __init__(self, game, number_level):
        self.number_level, self.game = number_level, game
        self.blocks_im = []
        self.spawn = Vector(0, 0)
        self.read_level(number_level)

        self.load_blocs()
        self.create_level_surface()

        self.start = round(datetime.today().timestamp())

    def load_blocs(self):
        self.blocks_im = []
        # Définir quel map a quel thème plus tard
        if 0 <= self.number_level <= 99:
            # À modifier quand on aura les assets par un for
            dirt = pg.image.load(get_asset("dirt_2.png"))
            dirt = dirt_variation = pg.transform.scale(dirt, (64, 64))
            for _ in range(4):
                dirt_variation = pg.transform.rotate(dirt_variation, -90)
                self.blocks_im.append(dirt_variation)

    def create_level_surface(self):
        """ Makes a pg Surface, that will be displayed over the background by Game """
        size = (len(self.level_array[0]) * 64, len(self.level_array) * 64)

        red_block = pg.Surface((64,64))
        red_block.fill((255,0,0))

        self.level_surface = pg.Surface(size)
        # Tells pg that every perfectly black pixel should be transparent, the hex of black pixels should be 010101
        self.level_surface.set_colorkey((0, 0, 0))

        for x in range(len(self.level_array[0])):
            for y in range(len(self.level_array)):
                if self.level_array[y][x] == 1:
                    self.level_surface.blit(random.choice(self.blocks_im), (x * 64, y * 64))
                elif self.level_array[y][x] == 2:
                    self.level_surface.blit(red_block, (x * 64, y * 64))

    def display(self):
        self.game.surface.blit(
            self.level_surface,
            (
                self.game.half_size[0] - self.game.player.pos.x,
                self.game.half_size[1] - self.game.player.pos.y
            )
        )

    def read_level(self, number_level):
        self.level_array = []
        # r+t: read as text file
        with open(get_asset("Levels/level_" + str(number_level) + ".lvl"), mode='r+t') as level_file:
            for (row, line) in enumerate(level_file):
                if line[-1] == '\n':
                    line = line[:-1]
                if row == 0:
                    # Transforms a string "x,y" into a tuple (x,y), with x,y int, and then into a vector
                    spawn = tuple(map(int, line.split(',')))
                    self.spawn = Vector.from_tuple(spawn)
                else:
                    self.level_array.append(list(map(int, line)))
