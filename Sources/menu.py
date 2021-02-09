import pygame as pg


class Menu():
    def __init__(self):
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()

        self.childs = []

    def display(self):
        for child in self.childs:
            child.display()

    def handleEvent(self, event):
        pass
