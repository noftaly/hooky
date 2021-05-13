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

        self.read_config()
        print(self.config)
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

    def read_config(self):
        self.config = []
        with open("./Assets/settings.cfg", mode="r+t") as config_f:
            i = 0
            for line in config_f:
                if line[-1] == '\n' or line[-1] == ' ':
                    line = line[:-1]
                if i == 0:
                    self.config.append(int(line))
                else:
                   self.config.append(list(map(int,line.split(' '))))
                i += 1
    def write_config(self):
        with open("./Assets/settings.cfg", mode="w+t") as config_f:
                config_f.write(str(self.config[0])+'\n')
                for i in range(4):
                        config_f.write(str(self.config[1][i])+' ')