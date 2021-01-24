import pygame as pg

class Player:
    def __init__(self, game, spn):
        self.game = game
        self.pos = spn[0]*64 + 32, spn[1]*64 + 32
        self.surf = pg.Surface((64,64)).fill((255,0,0)) #carré vert, pour le debugging