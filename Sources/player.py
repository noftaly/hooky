import pygame as pg

class Player:
    def __init__(self,spn):
        self.pos = spn[0]*64,spn[1]*64
        self.surf = pg.Surface((64,64)).fill((255,0,0)) #carré vert, pour le debugging