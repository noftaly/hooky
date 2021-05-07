import pygame as pg
from widget import Button

class Principal():
    def __init__(self, parent):
        self.parent = parent
        self.surf = parent.surf
        self.size = self.parent.size

        self.childs = []

        #Les gros bouttons du centre d'abord !
        self.childs.append(Button(self, (0,0), (0,0), True, self.play, "playb"))
        self.childs.append(Button(self, (0,0), (0,0), True, self.options, "opb"))
        self.childs.append(Button(self, (0,0), (0,0), True, self.quit, "quitb"))

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
            self.childs[i].pos = (960//ratio , 250//ratio + i*178//ratio)
            self.childs[i].update()

    def play(self):
        print("play !")
    
    def options(self):
        print("options !")

    def quit(self):
        print("quit !")
        self.parent.running = False