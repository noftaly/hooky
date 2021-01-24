import pygame as pg

class Player:
    def __init__(self, game, spn):
        self.game = game
        self.pos = spn[0]*64 + 32, spn[1]*64 + 32
    def display(self):
        pg.draw.circle(self.game.surf,(0,0,255),self.game.hsize,26)