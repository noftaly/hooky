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
        elif self.engaged and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.engaged = False
            self.bound()

class Checker():
    def __init__(self, parent, command):
        self.parent, self.command = parent, command
        self.to_disp = True
        self.state = True
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
            self.image.fill((0,255,255))
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
            self.state = not self.state
            self.command(self.state)
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

class KeyBinder():
    chars = {0 : '...', 27 : 'Esc', 178 : '²', 49 : '1', 50 : '2', 51 : '3', 52 : '4', 53 : '5', 54 : '6', 55 : '7', 56 : '8', 57 : '9', 48 : '0', 41 : ')', 61 : '=', 8 : 'Backspace', 9 : 'Tab', 97 : 'a', 122 : 'z', 101 : 'e', 114 : 'r', 116 : 't', 121 : 'y', 117 : 'u', 105 : 'i', 111 : 'o', 112 : 'p', 94 : '^', 36 : '$', 13 : 'Enter', 1073741881 : 'C.Lock', 113 : 'q', 115 : 's', 100 : 'd', 102 : 'f', 103 : 'g', 104 : 'h', 106 : 'j', 107 : 'k', 108 : 'l', 109 : 'm', 249 : '%', 42 : 'µ', 1073742049 : 'L Shift', 60 : '<', 119 : 'w', 120 : 'x', 99 : 'c', 118 : 'v', 98 : 'b', 110 : 'n', 44 : ',', 59 : ';', 58 : ':', 33 : '!', 1073742053 : 'R Shift', 1073742048 : 'L Ctrl', 1073742050 : 'L Alt', 32 : 'Space', 1073742054 : 'Fn', 1073742052 : 'R Ctrl', 1073741904 : 'Left', 1073741906 : 'Up', 1073741903 : 'Right', 1073741905 : 'Down', 127 : 'Suppr', 1073741897 : 'Ins', 1073741898 : 'Start', 1073741901 : 'End', 1073741902 : 'Pg. Down', 1073741899 : 'Pg. Up', 1073741922 : 'Keypad 0', 1073741923 : 'Keypad .', 1073741912 : 'Keypad Enter', 1073741913 : 'Keypad 1', 1073741914 : 'Keypad 2', 1073741915 : 'Keypad 3', 1073741916 : 'Keypad 4', 1073741917 : 'Keypad 5', 1073741918 : 'Keypad 6', 1073741911 : 'Keypad +', 1073741919 : 'Keypad 7', 1073741920 : 'Keypad 8', 1073741921 : 'Keypad 9', 1073741908 : 'Keypad /', 1073741909 : 'Keypad *', 1073741910 : 'Keypad -'}
    def __init__(self, parent, key):
        self.parent, self.key = parent, key

        self.to_disp = True
        self.engaged = False
        self.awaiting = False
        self.hovered = False

    def update(self):
        ratio = self.parent.parent.ratio

        self.image = pg.Surface(self.size)
        if self.hovered:
            self.image.fill((200,200,200))
        else:
            self.image.fill((255,255,255))

        #retrieves a Font object, asking for Option.ft (impact or default), renders the character corresponding to self.key and blits it onto self.image
        txt = pg.font.SysFont(self.parent.ft, 30//ratio).render(KeyBinder.chars[self.key], True, (0,0,0))
        size = txt.get_size()
        self.image.blit(txt, (self.size[0]//2,0))
        
    def display(self):
        self.update() #pas opti
        self.parent.surf.blit(self.image, self.pos)
        self.to_disp = False
    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, self.size, event.pos):
                self.to_disp = not self.hovered
                self.hovered = True
            else:
                self.to_disp = self.hovered
                self.hovered = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered
        elif self.engaged and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.awaiting = True
            self.engaged = False
            self.key = 0
            self.to_disp = True

        elif self.awaiting and event.type == pg.KEYDOWN:
            if event.key in KeyBinder.chars:
                self.key = event.key
                self.to_disp = True
                self.awaiting = False
