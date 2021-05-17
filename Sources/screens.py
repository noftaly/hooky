import pygame as pg
from vector import Vector
from utils import get_asset
from widget import Button, Checkbox, Slider, KeyBinder
from game import Game

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surface = parent.surface
        self.size = self.parent.size

        self.surface.blit(
            pg.transform.scale(
                pg.image.load(get_asset("menu_background.png")),
                (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio))
            ),
            (0, 0)
        )
        # Les gros bouttons du centre d'abord !
        self.childs = [
            Button(self, self.play, "Jouer"),
            Button(self, self.options, "Options"),
            Button(self, self.quit, "Quitter"),
        ]

        self.update()

    def display(self):
        for child in self.childs:
            if child.to_display:
                child.display()

    def handle_event(self,event):
        for child in self.childs:
            child.handle_event(event)

    def update(self):
        ratio = self.parent.ratio
        for i in range(3):
            self.childs[i].size = Vector(450 * ratio, 112 * ratio).with_ints()
            self.childs[i].pos = Vector(960 * ratio, 500 * ratio + i * 150 * ratio).with_ints()
            self.childs[i].update()

    def play(self):
        Game(self.parent, 1).main()
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

        self.font = self.parent.font

        self.background = pg.transform.scale(pg.image.load(get_asset("menu_background.png")), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))

        self.childs = [
            Checkbox(self, self.fullscreen, self.parent.config.get('fullscreen')),
            Slider(self, self.parent.config.get('volume')),
            KeyBinder(self, self.parent.config.get('keybinds')[0]),
            KeyBinder(self, self.parent.config.get('keybinds')[1]),
            KeyBinder(self, self.parent.config.get('keybinds')[2]),
            KeyBinder(self, self.parent.config.get('keybinds')[3]),
            Button(self, self.back, "back"),
        ]

        self.update()

    def display(self):
        if self.childs[1].to_display: #the slider needs the whole screen to be redrawn
            self.all_disp = True
        if self.all_disp:
            self.surface.blit(self.background, (0, 0))

        for child in self.childs:
            if child.to_display or self.all_disp:
                child.display()

        self.all_disp = False

    def handle_event(self, event):
        for child in self.childs:
            child.handle_event(event)

    def update(self):
        # Need to reload image from file, or scale will compress it
        self.background = pg.transform.scale(pg.image.load(get_asset("menu_background.png")), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))

        ratio = self.parent.ratio
        # Show captions
        text = self.font.render("Inputs", True, (0, 0, 0))
        self.background.blit(text, (int(600 * ratio), int(425 * ratio)))
        text = self.font.render("Left", True, (0, 0, 0))
        self.background.blit(text, (int(700 * ratio), int(485 * ratio)))
        text = self.font.render("Right", True, (0, 0, 0))
        self.background.blit(text, ((700 * ratio), int(545 * ratio)))
        text = self.font.render("Jump", True, (0, 0, 0))
        self.background.blit(text, (int(700 * ratio), int(605 * ratio)))
        text = self.font.render("Pause", True, (0, 0, 0))
        self.background.blit(text, (int(700 * ratio), int(665 * ratio)))

        text = self.font.render("Volume", True, (0, 0, 0))
        self.background.blit(text, (int(600 * ratio), int(778 * ratio)))
        text = self.font.render("Fullscreen", True, (0, 0, 0))
        self.background.blit(text, (int(600 * ratio), int(875 * ratio)))

        # Fullscreen checkbox
        self.childs[0].pos = Vector(1020 * ratio, 875 * ratio).with_ints()
        self.childs[0].size = Vector(50 * ratio, 50 * ratio).with_ints()
        # Volume slider
        self.childs[1].pos = Vector(950 * ratio, 778 * ratio).with_ints()
        self.childs[1].size = Vector(350 * ratio, 350 * ratio).with_ints()
        # Key inputs
        for i in range(4):
            self.childs[2+i].pos = Vector(950 * ratio, 485 * ratio + i * 60 * ratio).with_ints()
            self.childs[2+i].size = Vector(300 * ratio, 50 * ratio).with_ints()
            self.childs[2+i].update()

        # Back
        self.childs[6].pos = Vector(1450 * ratio, 60 * ratio).with_ints()
        self.childs[6].size = Vector(150 * ratio, 60 * ratio).with_ints()
        self.childs[6].update()

    def back(self):
        self.parent.active = Principal(self.parent)
        self.apply()
        del self

    def apply(self):
        keybinds_button = [elm for elm in self.childs if isinstance(elm, KeyBinder)]
        self.parent.config.update({
            'volume': self.childs[1].value,
            'fullscreen': self.childs[0].checked,
            'keybinds': list(map(lambda x: x.key, keybinds_button))
        })
        self.parent.write_config()

    def fullscreen(self, is_fullscreen):
        if is_fullscreen:
            pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
        else:
            pg.display.set_mode((1280,720))

        self.parent.surface = pg.display.get_surface()
        self.parent.size = Vector.from_tuple(self.parent.surface.get_size())
        self.parent.ratio = self.parent.size.x / 1920

        self.all_disp = True
        self.update()

class LevelSelector():
    def __init__(self):
        self.childs = []

    def display(self):
        for child in self.childs:
            if child.todisp:
                child.display()
