import pygame as pg
import time as t
from screens import Principal
"""
display() blits the right things onto Menu.surf
handle_event() updates the class variables in function of the input
update() updates the position/size (childs) or the image(self)

"""
class Menu():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.display.set_mode((1920,1080), pg.FULLSCREEN)
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()
        self.ratio = self.size[0] / 1920

        self.active = Principal(self)

        self.get_config()
        self.running = True
    def display(self):
        self.active.display()
        pg.display.update()

    def handle_event(self, event):
        if event.type  == pg.QUIT:
            self.running = False
        else:
            self.active.handle_event(event)
    
    def main(self):
        st = t.time()
        while self.running:
            self.display()
            for event in pg.event.get():
                self.handle_event(event)

    def get_config(self):
        # = [vol,disp settings,]
        pass
    
        #faire ca, puis faire display binder