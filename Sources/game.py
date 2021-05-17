import time
import pygame as pg

from level import Level
from player import Player

class Game:
    CELL_SIZE = 64

    def __init__(self, parent, number_level):
        self.parent = parent
        self.surface = pg.display.get_surface()
        self.size = self.surface.get_size()
        self.half_size = self.size[0] // 2, self.size[1] // 2

        # self.font = pg.font.SysFont('Helvetica', 30)
        self.background = pg.Surface(self.size)
        self.background.fill((0, 240, 240))

        self.level = Level(self, number_level)
        self.player = Player(self, self.level.spawn)

        self.config = self.parent.config
        self.left_key = self.config.get('keybinds')[0] # pg.K_LEFT
        self.right_key = self.config.get('keybinds')[1] # pg.K_RIGHT
        self.up_key = self.config.get('keybinds')[2] # pg.K_UP

        self.running = True

    def handle_event(self, event):
        if event.type == pg.QUIT:
            self.running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            self.player.launch_hook(event.pos)
        if event.type == pg.MOUSEBUTTONUP and event.button == 3:
            self.player.stop_hook()

    def display(self):
        """ Update the graphics """
        self.surface.blit(self.background, (0, 0))

        self.level.display()
        if self.player.hook.visible:
            self.player.hook.display()
        self.player.display()
        #self.show_hud()

        pg.display.update()

    # def show_hud(self):
    #     """ Create an HUD """
    #     surface = pg.Surface((250, 150))
    #     surface.fill(0x010101)
    #     time = self.font.render(f'Temps : {self.get_time()}', False, (255, 255, 255))
    #     level = self.font.render(f'Niveau : X', False, (255, 255, 255))
    #     attempt = self.font.render(f'Tentative : X', False, (255, 255, 255))
    #     surface.blit(time, (20, 20))
    #     surface.blit(level, (20, 60))
    #     surface.blit(attempt, (20, 100))

    #     self.surface.blit(surface, (10, 10))

    # def get_time(self):
    #     seconds = round(datetime.today().timestamp()) - self.level.start
    #     minutes = seconds // 60
    #     seconds %= 60
    #     print(f'{str(minutes).rjust(2, "0")}:{str(seconds).rjust(2, "0")}')
    #     return f'{str(minutes).rjust(2, "0")}:{str(seconds).rjust(2, "0")}'

    def next_level(self):
        self.running = False
        next_level = self.level.number_level + 1
        if next_level > Level.MAX_LEVEL:
            self.parent.start()
            self.parent.main()
        else:
            self.level = Level(self, self.level.number_level + 1)
            self.player = Player(self, self.level.spawn)
            self.running = True
            self.main()

    # NOTE: No PyGame object in update()!
    def update(self):
        """ Update entities """
        self.player.update()
        if self.player.hook.visible:
            self.player.hook.update()

    def main(self):
        while self.running:
            start_frame = time.time()

            self.display()
            self.update()
            for event in pg.event.get():
                self.handle_event(event)

            wait = 0.0083 - time.time() + start_frame
            if wait > 0:
                time.sleep(wait)
