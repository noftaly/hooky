import pygame as pg
from widget import Button, Checker, Slider

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surf = parent.surf
        self.size = self.parent.size

        self.childs = []

        self.surf.blit(pg.transform.scale(pg.image.load("../Assets/mbckg.png"),(1920//self.parent.ratio, 1080//self.parent.ratio)), (0,0))
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
            self.childs[i].size = (512//ratio, 128//ratio)
            self.childs[i].pos = (960//ratio - 120//ratio, 500//ratio + i*178//ratio)
            self.childs[i].update()

    def play(self):
        print("play !")
    
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

        self.bckg = pg.transform.scale(pg.image.load("../Assets/obckg.png"), (1920//self.parent.ratio, 1080//self.parent.ratio))
        self.childs = []
        self.childs.append(Checker(self))
        self.childs.append(Slider(self))

        self.update()

    def display(self):
        if self.childs[1].to_disp:
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


    