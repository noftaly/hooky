import random
import pygame as pg


class Level:
    def __init__(self, game, number_level):
        self.number_level, self.game = number_level, game
        self.read_level(number_level)
        
        self.load_blocs()
        self.mk_lvl_surf()

    def load_blocs(self):
        self.blocks_im = []
        if 0 <= self.number_level <= 99: #définir quel map as quel thème plus tard
            #à modifier quand on aura les assets
            b1 = pg.Surface((64,64))
            b1.fill((216, 106, 0))
            self.blocks_im.append(b1)

            b2 = pg.Surface((64,64))
            b2.fill((137,90,00))
            self.blocks_im.append(b2)

    
    def mk_lvl_surf(self): #Makes a pg Surface, that will be displayed over the background by Game
        px_size = len(self.level_array[0])*64,len(self.level_array)*64
        self.lvl_surf = pg.Surface(px_size)
        self.lvl_surf.set_colorkey((0,0,0)) #tells pg that every perfectly black pixel should be transparent, the hex of black pixel should be 010101

        for x in range(len(self.level_array[0])):
            for y in range(len(self.level_array)):
                if self.level_array[y][x] == 1:
                    self.lvl_surf.blit(random.choice(self.blocks_im),(x*64,y*64))
        

    def display(self): 
        self.game.surface.blit(self.lvl_surf,(
                                            self.game.half_size[0] - self.game.player.pos[0],
                                            self.game.half_size[1] - self.game.player.pos[1]
                                            ))

    def read_level(self, number_level):
        self.level_array = []
        # r+t: read as text file
        with open("../Levels/level_" + str(number_level) + ".lvl", mode='r+t') as level_file:
            for (row, line) in enumerate(level_file):
                if line[-1] == '\n':
                    line = line[:-1]
                if row == 0:
                    # Transforms a string "x,y" into a tuple (x,y), with x,y int
                    self.spawn = tuple(map(int, line.split(',')))
                else:
                    self.level_array.append(list(map(int,line)))
