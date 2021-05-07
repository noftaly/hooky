import pygame as pg

def is_in(pos,size,coords):
    if ((pos[0] <= coords[0] <= pos[0] + size[0])
        and (pos[1] <= coords[1] <= pos[1] + size[1])):
            return True
    return False

class Button():
    def __init__(self, parent, pos, size,centered, bind, name):
        self.parent, self.pos, self.size, self.centered, self.bound, self.name = parent, pos, size, centered, bind, name


        self.to_disp = True
        self.hovered = False
        self.engaged = False
    

    def display(self):
        self.parent.surf.blit(self.image,self.pos)
        if self.hovered:
            self.parent.surf.blit(self.mask,self.pos)
        self.to_disp = False

    def update(self):
        print("updated!", self.name)
        half_size = (self.size[0]//2, self.size[1]//2)
        #changes the blitpos
        if self.centered:
            self.pos = (self.pos[0] - half_size[0],
                            self.pos[1] - half_size[1])

        self.mask = pg.Surface(self.size)
        self.mask.set_alpha(50)

        try:
            self.image = pg.transform.scale(pg.image.load("./Assets/"+self.name+".png"),self.size)
        except:
            self.image = pg.transform.scale(pg.image.load("../Assets/missing.png"),self.size)

    def handle_event(self,event): #only pass mouse events !
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, self.size, event.pos):
                self.to_disp = not self.hovered
                self.hovered = True
            else:
                self.to_disp = self.hovered
                self.hovered = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.engaged and self.hovered:
            self.engaged = False
            self.bound()



