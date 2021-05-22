import pygame as pg
from music_manager import change_volume
from vector import Vector
from utils import get_asset
from widget import Button, Checkbox, Slider, KeyBinder
from game import Game
from gc import collect

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
            Button(self, self.parent.play, "Jouer"),
            Button(self, self.select, "Niveaux"),
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
        for (i, child) in enumerate(self.childs):
            child.size = Vector(450 * ratio, 112 * ratio).with_ints()
            child.pos = Vector(960 * ratio, 500 * ratio + i * 150 * ratio).with_ints()
            child.update()

    def select(self):
        self.parent.active = LevelSelector(self.parent, 5)

    def options(self):
        self.parent.active = Options(self.parent)

    def quit(self):
        self.parent.stop()

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
            Slider(self, self.parent.config.get('volume'), change_volume),
            KeyBinder(self, self.parent.config.get('keybinds')[0]),
            KeyBinder(self, self.parent.config.get('keybinds')[1]),
            KeyBinder(self, self.parent.config.get('keybinds')[2]),
            KeyBinder(self, self.parent.config.get('keybinds')[3]),
            Button(self, self.save, "Save"),
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
        self.childs[1].size = Vector(350 * ratio, 8 * ratio).with_ints()
        # Key inputsd
        for i in range(4):
            self.childs[2+i].pos = Vector(950 * ratio, 485 * ratio + i * 60 * ratio).with_ints()
            self.childs[2+i].size = Vector(300 * ratio, 50 * ratio).with_ints()
            self.childs[2+i].update()

        # Back
        # I CAN'T FKCING CENTER IT OMGGG
        self.childs[6].size = Vector(250 * ratio, 60 * ratio).with_ints()
        self.childs[6].pos = Vector(690 * ratio, 1000 * ratio).with_ints()
        self.childs[6].update()

    def save(self):
        self.parent.active = Principal(self.parent)
        self.apply()
        del self
        collect()

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
    def __init__(self, parent, levels_amount):
        self.parent = parent
        self.surface = parent.surface
        self.size = self.parent.size

        self.background = pg.transform.scale(pg.image.load(get_asset("menu_background.png")), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))

        self.childs = []
        for i in range(levels_amount):
            start_level = lambda i=i: self.start_level(i + 1)
            self.childs.append(Button(self, start_level, f"Niveau {i + 1}"))

        self.childs.append(Button(self, self.back, "Retour"))
        self.update()

    def display(self):
        for child in self.childs:
            if child.to_display:
                child.display()

    def handle_event(self, event):
        for child in self.childs:
            child.handle_event(event)

    def update(self):
        self.surface.blit(self.background, (0, 0))
        # Need to reload image from file, or scale will compress it
        self.background = pg.transform.scale(pg.image.load(get_asset("menu_background.png")), (int(1920 * self.parent.ratio), int(1080 * self.parent.ratio)))

        ratio = self.parent.ratio
        aligns = { 'left': 700 * ratio, 'right': 1200 * ratio }
        column = 0
        for (i, child) in enumerate(self.childs[:-1]):
            is_right = i % 2 == 1
            alignement = aligns['right' if is_right else 'left']
            child.size = Vector(350 * ratio, 98 * ratio).with_ints()
            child.pos = Vector(alignement, 500 * ratio + column * 150 * ratio).with_ints()
            child.update()
            if is_right:
                column += 1

        # Back
        # I CAN'T FKCING CENTER IT OMGGG
        last = self.childs[-1]
        last.size = Vector(300 * ratio, 80 * ratio).with_ints()
        total_size = Vector.from_tuple(self.parent.surface.get_size()) // 2
        last.pos = Vector(total_size.x - last.size.x // 2, 1000).with_ints()
        last.update()

    def start_level(self, number):
        self.parent.game = Game(self.parent, number, False)
        self.parent.game.main()
        self.parent.stop()

    def back(self):
        self.parent.active = Principal(self.parent)
        del self
        collect()

class Pause():
    def __init__(self, parent):
        self.parent = parent
        ratio = parent.ratio
        if not pg.display.get_init():
            pg.display.init()
        self.surface = parent.surface

        self.image = pg.Surface(
            (int(400*ratio), int(400*ratio))
            )
        self.image.fill((210, 224, 125))
        text = parent.font.render("Pause",True,(0,0,0))
        self.image.blit(text,(int(150*ratio),int(30*ratio)))

        self.childs = [
            Button(self, self.parent.resume,"Resume"),
            Button(self, self.parent.back, "Back")

        ]
        
        self.surface.blit(self.image,(int(760*ratio),int(162*ratio)))
        

        self.childs[0].pos = Vector(960*ratio,350*ratio).with_ints()
        self.childs[0].size = Vector(250*ratio,80*ratio).with_ints()
        self.childs[0].update()

        self.childs[1].pos = Vector(960*ratio,450*ratio).with_ints()
        self.childs[1].size = Vector(250*ratio,80*ratio).with_ints()
        self.childs[1].update()

    def display(self):
        for child in self.childs:
            if child.to_display:
                child.display()
    
    def handle_event(self,event):
        if event.type == pg.KEYDOWN and event.key == self.parent.config['keybinds'][3]:
                self.parent.resume()
        else:
            for child in self.childs:
                child.handle_event(event)