import pygame as pg
from screens import Principal

class Menu():
    def __init__(self):
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()
        self.ratio = 1920 // self.size[0]

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
        while self.running:
            self.display()
            for event in pg.event.get():
                self.handle_event(event)

    def get_config(self):
        # = [vol,disp settings,]
        pass

pg.init()
pg.display.set_mode((1920, 1080))
Menu().main()