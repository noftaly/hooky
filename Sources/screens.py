import pygame as pg
from widget import Button, Checker, Slider, KeyBinder
from game import Game

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surf = parent.surf
        self.size = self.parent.size

        self.childs = []
        self.surf.blit(pg.transform.scale(pg.image.load("./Assets/mbckg.png"),(int(1920//self.parent.ratio), int(1080//self.parent.ratio))), (0,0))
        #Les gros bouttons du centre d'abord !
        self.childs.append(Button(self, True, self.play, "playb"))
        self.childs.append(Button(self, True, self.options, "opb"))
        self.childs.append(Button(self, True, self.quit, "quitb"))

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
            self.childs[i].size = (int(450*ratio),int(112*ratio))
            self.childs[i].pos = (int(960*ratio),int(500*ratio) + i*150*ratio)
            self.childs[i].update()

    def play(self):
        Game(0).main()
        self.parent.running = False #Will be executed only if the Game.main() is broke by an alt+f4
    
    def options(self):
        self.parent.active = Options(self.parent)

    def quit(self):
        self.parent.running = False

    

class Options():
    def __init__(self, parent):
        self.parent = parent
        self.surf = parent.surf
        self.size = self.parent.size

        if 'impact' in pg.font.get_fonts():
            self.ft = 'impact'
        else:
            self.ft = pg.font.get_default_font()

        self.bckg = pg.transform.scale(pg.image.load("./Assets/obckg.png"), (int(1920//self.parent.ratio), int(1080//self.parent.ratio)))
        self.childs = []
        self.childs.append(Checker(self,self.fullscreen))
        self.childs.append(Slider(self))
        self.childs.append(KeyBinder(self,97))
        self.update()

    def display(self):
        if self.childs[1].to_disp: #the slider needs the whole screen to be redrawn
            self.surf.blit(self.bckg,(0,0))

        for child in self.childs:
            if child.to_disp or self.all_disp:
                child.display()
        
        self.all_disp = False
        

    def handle_event(self, event):
        for child in self.childs:
            child.handle_event(event)
    def update(self):
        ratio = self.parent.ratio
        print("ratio", ratio)
        self.childs[0].pos = (int(1020*ratio),int(875*ratio))
        self.childs[0].size = int(50*ratio)
        self.childs[1].pos = (int(950*ratio),int(778*ratio))
        self.childs[1].size = int(350*ratio)
        #for i in range(4):
        self.childs[2].pos = (int(950*ratio),int(500*ratio))
        self.childs[2].size = (int(300*ratio),int(50*ratio))
        self.childs[2].update()

    def fullscreen(self, mode):
        if mode:
            pg.display.set_mode((1920,1080), pg.FULLSCREEN)
        else:
            pg.display.set_mode((1280,720))
        
        self.parent.surf = pg.display.get_surface()
        self.parent.size = self.parent.surf.get_size()
        print(self.parent.size)
        self.parent.ratio = self.parent.size[0] / 1920

        self.update()
        self.display()