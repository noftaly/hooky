import pygame as pg

def is_in(pos,size,coords):
    if ((pos[0] <= coords[0] <= pos[0] + size[0])
        and (pos[1] <= coords[1] <= pos[1] + size[1])):
            return True
    return False

class Button():
    def __init__(self, parent,centered, bind, name):
        self.parent, self.centered, self.bound, self.name = parent, centered, bind, name

        try:
            self.image = pg.image.load("./Assets/"+self.name+".png")
        except:
            self.image = pg.image.load("./Assets/missing.png")
        self.to_disp = True
        self.hovered = False
        self.engaged = False
    

    def display(self):
        self.parent.surf.blit(self.image,self.pos)
        if self.hovered:
            self.parent.surf.blit(self.mask,self.pos)
        self.to_disp = False

    def update(self):
        half_size = (self.size[0]//2, self.size[1]//2)
        #changes the blitpos
        if self.centered:
            self.pos = (self.pos[0] - half_size[0],
                            self.pos[1] - half_size[1])

        self.mask = pg.Surface(self.size)
        self.mask.set_alpha(80)

        self.image = pg.transform.scale(self.image,self.size)

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

class Binder():
    def __init__(self,parent):
        self.parent = parent
        
        self.to_disp = True
        self.hovered = False

    def update():
        pass


class Checker():
    def __init__(self, parent):
        self.parent = parent

        self.to_disp = True
        self.state = False
        self.hovered = False
        self.engaged = False
    def display(self):
        self.update()
        self.parent.surf.blit(self.image,self.pos)
        self.to_disp = False

    def update(self):
        ratio = self.parent.parent.ratio
        self.image = pg.Surface((self.size,self.size))
        if self.hovered:
            self.image.fill((0,150,150))
        pg.draw.rect(self.image, (255,255,255),(4//ratio,4//ratio,self.size-8//ratio,self.size-8//ratio))
        if self.state:
            pg.draw.rect(self.image, (0,0,0),(10//ratio,10//ratio,self.size-20//ratio,self.size-20//ratio))
    
    def handle_event(self,event):
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, (self.size, self.size), event.pos):
                self.to_disp = not self.hovered
                self.hovered = True
            else:
                self.to_disp = self.hovered
                self.hovered = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.engaged and self.hovered:
            self.engaged = False
            self.to_disp = True
            self.fullscreen()
    def fullscreen(self):
        self.state = not self.state
        pass

class Slider():
    def __init__(self, parent):
        self.parent = parent
        
        self.vol = 500
        self.engaged = False
        self.to_disp = True

    def display(self):
        ratio = self.parent.parent.ratio
        pg.draw.line(self.parent.surf, (50,50,50),
                    (self.pos[0], self.pos[1]),
                    (self.pos[0] + (self.size*self.vol)//1000, self.pos[1]),
                    8//ratio)
        pg.draw.line(self.parent.surf, (150,150,150),
                    (self.pos[0] + (self.size*self.vol)//1000, self.pos[1]),
                    (self.pos[0] + self.size, self.pos[1]),
                    8//ratio)
        pg.draw.circle(self.parent.surf, (50,50,50), (self.pos[0] + (self.size*self.vol)//1000,self.pos[1]), 25//ratio)
        self.to_disp = False

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION and self.engaged:
            if event.pos[0] <= self.pos[0]:
                self.vol = 0
            elif event.pos[0] >= self.pos[0] + self.size:
                self.vol = 1000
            else:
                self.vol = int(((event.pos[0] - self.pos[0])/self.size)*1000)
            self.to_disp = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            ratio = self.parent.parent.ratio
            if is_in(event.pos, (48/ratio,48/ratio), (self.pos[0] + (self.size*self.vol)//1000 + 24/ratio, self.pos[1] + 24/ratio)):
                self.engaged = True
        elif event.type == pg.MOUSEBUTTONUP and self.engaged:
            self.engaged = False
