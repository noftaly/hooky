import pygame as pg

class Menu():
    def __init__(self):
        self.surf = pg.display.get_surface()
        self.size = self.surf.get_size()

        self.childs = []

        self.running = True

    def display(self):
        #self.bckg.display() animé plus tard
        self.surf.fill((54,186,223))
        for child in self.childs:
            child.display()
        
        pg.display.update()

    def handle_event(self, event):
        if event.type  == pg.quit():
            self.running = False
        else:
            for child in self.childs:
                child.handle_event(event)



            


Menu().main()
