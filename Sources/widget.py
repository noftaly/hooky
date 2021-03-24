import pygame as pg



def is_in(pos,size,coords):
    if (pos[0] <= coords[0] <= pos[0] + size[0])
        and (pos[1] <= coords[1] <= pos[1] + size[1]):
            return True
    return False
class Button():
    def __init__(self, parent, pos, size, command, centered):
        self.parent, self.pos, self.size, self.command = parent, pos, size, command
        half_size = (self.size[0]//2,self.size[1]//2)
        if self.centered:
            self.blitpos = (self.pos[0]-half_size[0],
                            self.pos[1]-.half_size[1])

        self.hovered = False
        self.engaged = False
        self.resized = False # so you can add an image after initializing.
    
    def resize(self):
        try:
            pg.transform.scale(self.image,self.size)
        except:
            self.image = pg.Surface(self.size)
            self.image.fill((255,0,0))

    def display(self):
        self.parent.surface.blit(self.image,self.blitpos)

    def handle_event(self,event): #only pass mouse events !
        if is_in(self.pos,self.size,event.pos):
            self.hovered = True
            if event.button = 1:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.
        else:
            self.



