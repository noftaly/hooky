import pygame as pg
from screens import Principal

class Menu():
    """
    display() blits the right things onto Menu.surface
    handle_event() updates the class variables in function of the input
    update() updates the position/size (childs) or the image(self)
    """
    def __init__(self):
        pg.init()
        pg.font.init()

        self.read_config()
        if self.config[1]:
            pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
        else:
            pg.display.set_mode((1280, 720))

        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.ratio = self.size[0] / 1920

        self.active = Principal(self)

        self.running = True

    def display(self):
        self.active.display()
        pg.display.update()

    def handle_event(self, event):
        if event.type == pg.QUIT:
            self.running = False
        else:
            self.active.handle_event(event)

    def main(self):
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
                elif i == 1:
                    self.config.append(bool(int(line)))
                else:
                    self.config.append(list(map(int,line.split(' '))))
                i += 1

    def write_config(self):
        with open("./Assets/settings.cfg", mode="w+t") as config_f:
            config_f.write(str(self.config[0])+'\n')
            if self.config[1]:
                config_f.write('1\n')
            else:
                config_f.write('0\n')
            for i in range(4):
                config_f.write(str(self.config[2][i]) + ' ')
