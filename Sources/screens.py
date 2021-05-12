import pygame as pg
from widget import Button, Checker, Slider, KeyBinder
from game import Game

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surf = parent.surf
        self.size = self.parent.size

        self.childs = []

        self.surf.blit(pg.transform.scale(pg.image.load("./Assets/mbckg.png"),(1920//self.parent.ratio, 1080//self.parent.ratio)), (0,0))
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
            self.childs[i].size = (450//ratio, 112//ratio)
            self.childs[i].pos = (960//ratio,500 //ratio + i*150//ratio)
            self.childs[i].update()

    def play(self):
        Game(0).main()
    
    def options(self):
        self.parent.active = Options(self.parent)

    def quit(self):
        print("quit !")
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

        self.bckg = pg.transform.scale(pg.image.load("./Assets/obckg.png"), (1920//self.parent.ratio, 1080//self.parent.ratio))
        self.childs = []
        self.childs.append(Checker(self))
        self.childs.append(Slider(self))
        self.childs.append(KeyBinder(self,97))
        self.update()

    def display(self):
        if self.childs[1].to_disp: #the slider needs the whole screen to be redrawn
            self.surf.blit(self.bckg,(0,0))
            all_disp = True
        else:
            all_disp = False
        for child in self.childs:
            if child.to_disp or all_disp:
                child.display()

    def handle_event(self, event):
        for child in self.childs:
            child.handle_event(event)
    def update(self):
        ratio = self.parent.ratio
        self.childs[0].pos = (1020//ratio, 875//ratio)
        self.childs[0].size = 50//ratio
        self.childs[1].pos = (950//ratio, 778//ratio)
        self.childs[1].size = 350//ratio
        #for i in range(4):
        self.childs[2].pos = (950//ratio, 500//ratio)
        self.childs[2].size = (300//ratio, 50//ratio)
        self.childs[2].update()


    