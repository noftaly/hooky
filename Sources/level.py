import pygame as pg
from vector import Vector


class Level:
    def __init__(self, game, number_level):
        self.game = game
        self.readLevel(number_level)

        self.blocks = [] #y stocker les sprites de block en fonction du niveau

    def display(self): #CA MARCHE UN PEU
        pos = self.game.player.pos
        tpLft = Vector(pos.x//64 - 15, pos.y//64 - 8)
        if tpLft.x < 0:
            tpLft = Vector(0, tpLft.y)

        if tpLft.y < 0:
            tpLft = Vector(tpLft.x, 0)

        if tpLft.x + 31 >= len(self.lvAr[0]):
            rngX = len(self.lvAr[0]) - tpLft.x
        else:
            rngX = 31

        if tpLft.y + 18 >= len(self.lvAr):
            rngY = len(self.lvAr) - tpLft.y
        else:
            rngY = 18

        hlsz = self.game.hsize
        for i in range(rngX): # roundup(1920 / 64) + 1
            for j in range(rngY): # roundup(1080/64) + 1
                x = ((i + tpLft.x) * 64 + hlsz[0]) - pos.x
                y = ((j + tpLft.y) * 64 + hlsz[1]) - pos.y

                # Dirt
                if self.lvAr[tpLft.y+j][tpLft.x+i] == 1:
                    pg.draw.rect(self.game.surface, (101, 67, 33), (x, y, 64,64))
                # Sky
                elif self.lvAr[tpLft.y+j][tpLft.x+i] == 0:
                    pg.draw.rect(self.game.surface, (119, 181, 254), (x, y, 64,64))

    def update(self):
        pass

    def readLevel(self, number_level):
        self.lvAr = []
        # lvl is the lvl number / r+t => read as text file
        with open("./Levels/level_" + str(number_level) + ".lvl", mode='r+t') as levelFile:
            i = 0
            for line in levelFile:
                if line[-1] == '\n':
                    line = line[:-1]
                if i == 0:
                    # Transforms a string "(x,y)" into a tuple (x,y), with x,y int
                    self.spawn = Vector(*map(int, line[1:-1].split(',')))
                elif line[0] != '(':
                    # Adds the row converted into integers to lvAr
                    self.lvAr.append(list(map(int,line)))
                else:
                    # On vera pour les objets custom plus tard (objets déplaçables, texte etc.. )
                    pass
                i += 1
