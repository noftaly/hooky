import pygame as pg
import time as t
"""


"""

class Level:
    def __init__(self, game, nlvl):
        self.game = game
        self.readLvl(nlvl)

        self.blocks = [] #y stocker les sprites de block en fonction du niveau


    def display(self): #CA MARCHE UN PEU
        
        pos = self.game.plr.pos
        tpLft = pos[0]//64 - 15 ,pos[1]//64 - 8
        if tpLft[0] < 0:
            tpLft = 0,tpLft[1]
        
        if tpLft[1] < 0:
            tpLft = tpLft[0],0

        if tpLft[0]+31 >= len(self.lvAr[0]):
            rngX = len(self.lvAr[0]) - tpLft[0]
        else:
            rngX = 31

        if tpLft[1]+18 >= len(self.lvAr):
            rngY = len(self.lvAr) - tpLft[1]
        else:
            rngY = 18

        hlsz = self.game.hsize
        for i in range(rngX): # roundup(1920 / 64) + 1
            for j in range(rngY): # roundup(1080/64) + 1
                if self.lvAr[tpLft[1]+j][tpLft[0]+i] == 1:
                    if (i+j) % 2 == 0:
                        pg.draw.rect(self.game.surf,(255,0,0),(((i+tpLft[0])*64 + hlsz[0])-pos[0],((j+tpLft[1])*64 + hlsz[1])-pos[1],64,64))
                    else:
                        pg.draw.rect(self.game.surf,(0,255,0),(((i+tpLft[0])*64 + hlsz[0])-pos[0],((j+tpLft[1])*64 +  hlsz[1])-pos[1],64,64))
        

    def update(self):
        pass



    def readLvl(self, lvl):
        self.lvAr = []
        # lvl is the lvl number / r+t => read as text file
        with open("./Levels/level_" + str(lvl) + ".lvl", mode='r+t') as levelFile:
            i = 0
            for line in levelFile:
                if line[-1] == '\n':
                    line = line[:-1]
                if i == 0:
                    # Transforms a string "(x,y)" into a tuple (x,y), with x,y int
                    self.spn = tuple(map(int,line[1:-1].split(',')))
                elif line[0] != '(':
                    # Adds the row converted into integers to lvAr
                    self.lvAr.append(list(map(int,line)))
                else:
                    # On vera pour les objets custom plus tard (objets déplaçables, texte etc.. )
                    pass
                i += 1
