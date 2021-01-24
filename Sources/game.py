import pygame as pg
import time as t

from level import Level
from player import Player
from threading import Thread as th

class Game:
    def __init__(self,nlvl):
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()

        self.lvl = Level(self,nlvl)
        self.plr = Player(self,self.lvl.spn)
        self.running = True

        self.inpt = [False,False,False] #jump,left,right
    def handleEvent(self): #changes proprieties in function of the input
        pass
    def display(self): #sûrement sur un autre thread
        self.lvl.display()
        #self.plr.display()
    #AUCUN OBJET PG DANS UPDATE !!!
    def update(self): #next tick (ajout de toute les accélérations aux vitesses et ajout de toute les vitesses aux positions)
        pass
    def main(self):
        while self.running:
            stFrame = t.time()

            self.display()
            #th.Thread(target=self.display())
            self.update()
            for event in pg.event.get():
                self.handleEvent(event) 


            endFrame = t.time()
            if endFrame - stFrame < 0.0167:
                t.sleep(0.016 - endFrame + stFrame)
            else:
                print("OPTI FDP")
