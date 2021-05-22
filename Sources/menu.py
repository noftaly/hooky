import pygame as pg
from game import Game
from music_manager import play_menu_theme, stop_music
from screens import Principal, Pause
from vector import Vector
from utils import get_asset
from gc import collect

class Menu():
    """
    display() blits the right things onto Menu.surface
    handle_event() updates the class variables in function of the input
    update() updates the position/size (childs) or the image(self)
    """
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.font = pg.font.Font(get_asset("Hooky-Regular.ttf"), 48)

        self.read_config()
        pg.mixer.music.set_volume(self.config.get('volume') / 1000)
        if self.config.get('fullscreen'):
            pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
        else:
            pg.display.set_mode((1280, 720))

        self.surface = pg.display.get_surface()
        self.size = Vector.from_tuple(self.surface.get_size())
        self.ratio = self.size.x / 1920
        self.active = Principal(self)
        self.running = True
        play_menu_theme()


    def display(self):
        self.active.display()
        pg.display.update()

    def handle_event(self, event):
        if event.type == pg.QUIT:
            self.stop()
        else:
            self.active.handle_event(event)

    def main(self):
        while self.running:
            self.display()
            for event in pg.event.get():
                self.handle_event(event)
    def play(self):
        self.game = Game(self, 1, True)
        self.game.main()
        #triggers when a clean exit is done (esc + quit)
    def stop(self):
        self.running = False
        stop_music()

    def pause(self):
        self.game.running = False
        self.active = Pause(self)
    
    def back(self):
        del self.active
        del self.game
        #je sais pas pourquoi mais faut activement gc (le jeu pèse ~100 mb, si on spam back => play on tape vite le giga)
        collect()
        self.active = Principal(self)

    def resume(self):
        del self.active
        collect()
        self.game.running = True
        self.game.pause = False
        self.game.main()

    def read_config(self):
        self.config = {
            'volume': 0,
            'fullscreen': True,
            'keybinds': []
        }
        with open(get_asset("settings.cfg"), mode="r+t") as config_f:
            i = 0
            for line in config_f:
                if line[-1] == '\n' or line[-1] == ' ':
                    line = line[:-1]
                if i == 0:
                    self.config.update({ 'volume': int(line) })
                elif i == 1:
                    self.config.update({ 'fullscreen': bool(int(line)) })
                else:
                    self.config.update({ 'keybinds': list(map(int,line.split(' '))) })
                i += 1

    def write_config(self):
        with open(get_asset("settings.cfg"), mode="w+t") as config_f:
            config_f.write(str(self.config.get('volume')) + '\n')
            config_f.write(str(self.config.get('fullscreen').bit_length()) + '\n')
            config_f.write(' '.join(map(str, self.config.get('keybinds'))))
