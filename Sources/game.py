import pygame as pg
import time as t

from level import Level
from player import Player
from threading import Thread as th

class Game:
    def __init__(self,nlvl):
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()
        self.hsize = self.size[0]/2,self.size[1]/2

        self.lvl = Level(self,nlvl)
        self.plr = Player(self,self.lvl.spn)
        self.running = True

        self.inpt = [False,False,False] #jump,left,right
        
    def handleEvent(self): #changes proprieties in function of the input
        pass
    def display(self): #sûrement sur un autre thread
        self.surf.fill((0,0,0))
        self.lvl.display()
        self.plr.display()

        pg.display.update()
    #AUCUN OBJET PG DANS UPDATE !!!
    def update(self): #next tick (ajout de toute les accélérations aux vitesses et ajout de toute les vitesses aux positions)
        pass
    def main(self):
        i = 0
        while self.running:
            stFrame = t.time()
            self.display()
            #th.Thread(target=self.display())
            self.update()
            """
            for event in pg.event.get():
                self.handleEvent(event) """
            pg.event.clear()

            self.plr.pos = (i,i)
            i += 5
            endFrame = t.time()
            if endFrame - stFrame < 0.0167:
                t.sleep(0.0167 - endFrame + stFrame)
                print((endFrame - stFrame)*1000,"ms")
            else:
                print("OPTI FDP")
