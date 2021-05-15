import pygame as pg
from widget import Button, Checker, Slider, KeyBinder
from game import Game

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surface = parent.surface
        self.size = self.parent.size

        self.childs = []
        self.surface.blit(
            pg.transform.scale(
                pg.image.load("./Assets/mbckg.png"),
                (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio))
            ),
            (0, 0)
        )
        # Les gros bouttons du centre d'abord !
        self.childs.append(Button(self, self.play, "playb"))
        self.childs.append(Button(self, self.options, "opb"))
        self.childs.append(Button(self, self.quit, "quitb"))

        self.update()

    def display(self):
        for child in self.childs:
            if child.to_disp:
                child.display()

    def handle_event(self,event):
        for child in self.childs:
            child.handle_event(event)

    def update(self):
        ratio = self.parent.ratio
        for i in range(3):
            self.childs[i].size = (int(450 * ratio), int(112 * ratio))
            self.childs[i].pos = (int(960 * ratio), int(500 * ratio) + i * 150 * ratio)
            self.childs[i].update()

    def play(self):
        Game(self.parent, 0).main()
        self.parent.running = False # Will be executed only if the Game.main() is broke by an alt+f4

    def options(self):
        self.parent.active = Options(self.parent)

    def quit(self):
        self.parent.running = False

class Options():
    def __init__(self, parent):
        self.parent = parent
        self.surface = parent.surface
        self.size = self.parent.size
        self.all_disp = False

        if 'impact' in pg.font.get_fonts():
            self.font = 'impact'
        else:
            self.font = pg.font.get_default_font()

        self.background = pg.transform.scale(pg.image.load("./Assets/obckg.png"), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))
        self.childs = []
        self.childs.append(Checker(self, self.fullscreen, self.parent.config[1]))
        self.childs.append(Slider(self, self.parent.config[0]))
        self.childs.append(KeyBinder(self, self.parent.config[2][0]))
        self.childs.append(KeyBinder(self, self.parent.config[2][1]))
        self.childs.append(KeyBinder(self, self.parent.config[2][2]))
        self.childs.append(KeyBinder(self, self.parent.config[2][3]))
        self.childs.append(Button(self, self.back, "back"))
        self.update()

    def display(self):
        if self.childs[1].to_disp: #the slider needs the whole screen to be redrawn
            self.all_disp = True
        if self.all_disp:
            self.surface.blit(self.background, (0, 0))

        for child in self.childs:
            if child.to_disp or self.all_disp:
                child.display()

        self.all_disp = False

    def handle_event(self, event):
        for child in self.childs:
            child.handle_event(event)

    def update(self):
        # Need to reload image from file, or scale will compress it
        self.background = pg.transform.scale(pg.image.load("./Assets/obckg.png"), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))

        ratio = self.parent.ratio
        self.childs[0].pos = (int(1020 * ratio),int(875 * ratio))
        self.childs[0].size = int(50 * ratio)
        self.childs[1].pos = (int(950 * ratio),int(778 * ratio))
        self.childs[1].size = int(350 * ratio)
        for i in range(4):
            self.childs[2+i].pos = (int(950 * ratio),int(485 * ratio + i * 60 * ratio))
            self.childs[2+i].size = (int(300 * ratio),int(50 * ratio))
            self.childs[2+i].update()

        self.childs[6].pos = (int(1450 * ratio), int(60 * ratio))
        self.childs[6].size = (int(150 * ratio), int(60 * ratio))
        self.childs[6].update()

    def back(self):
        self.parent.active = Principal(self.parent)
        self.apply()
        del self

    def apply(self):
        self.parent.config[0] = self.childs[1].vol
        self.parent.config[1] = self.childs[0].state
        for i in range(4):
            self.parent.config[2][i] = self.childs[2+i].key

        self.parent.write_config()

    def fullscreen(self, mode):
        if mode:
            pg.display.set_mode((1920,1080), pg.FULLSCREEN)
        else:
            pg.display.set_mode((1280,720))

        self.parent.surface = pg.display.get_surface()
        self.parent.size = self.parent.surface.get_size()
        self.parent.ratio = self.parent.size[0] / 1920

        self.all_disp = True
        self.update()

class Level_Selec():
    def __init__(self):
        pass
    def display(self):
        for child in self.childs:
            if child.todisp:
                child.display()
