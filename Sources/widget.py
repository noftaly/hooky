import pygame as pg
from vector import Vector
from utils import get_asset

def is_in(pos, size, coords):
    if isinstance(pos, tuple): pos = Vector.from_tuple(pos)
    if isinstance(size, tuple): size = Vector.from_tuple(size)
    if isinstance(coords, tuple): coords = Vector.from_tuple(coords)

    return (pos.x <= coords.x <= pos.x + size.x) and (pos.y <= coords.y <= pos.y + size.y)

class Widget():
    def __init__(self, parent):
        self.parent = parent
        self.pos = Vector(0, 0)
        self.size = Vector(0, 0)
        self.hovered = False
        self.engaged = False
        self.to_display = True

        self.image = None

class Button(Widget):
    def __init__(self, parent, on_click, name):
        super().__init__(parent)

        self.on_click, self.name = on_click, name
        self.font = self.parent.parent.font

        try:
            self.image = pg.image.load(get_asset("button_background.png"))
            text = self.font.render(self.name, True, (255, 255, 255))
            text_size = Vector.from_tuple(text.get_size())
            image_size = Vector.from_tuple(self.image.get_size())
            pos = (image_size - text_size) // 2
            self.image.blit(text, pos.as_tuple())
        except FileNotFoundError:
            self.image = pg.image.load(get_asset("missing.png"))

        self.mask = None

    def display(self):
        self.parent.surface.blit(self.image, self.pos.as_tuple())
        self.parent.surface.blit(self.image, self.pos.as_tuple())
        if self.hovered:
            self.parent.surface.blit(self.mask, self.pos.as_tuple())
        self.to_display = False

    def update(self):
        self.pos -= self.size // 2

        self.mask = pg.Surface(self.size.as_tuple())
        self.mask.set_alpha(80)

        self.image = pg.transform.scale(self.image, self.size.as_tuple())

    def handle_event(self, event): # Only pass mouse events !
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, self.size, event.pos):
                self.to_display = not self.hovered
                self.hovered = True
            else:
                self.to_display = self.hovered
                self.hovered = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered

        elif self.engaged and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.engaged = False
            self.on_click()

class Checkbox(Widget):
    def __init__(self, parent, command, checked):
        super().__init__(parent)
        self.command, self.checked = command, checked

    def display(self):
        self.update()
        self.parent.surface.blit(self.image, self.pos.as_tuple())
        self.to_display = False

    def update(self):
        ratio = self.parent.parent.ratio
        self.image = pg.Surface(self.size.as_tuple())
        if self.hovered:
            self.image.fill((150, 150, 150))

        pg.draw.rect(
            self.image, (255, 255, 255),
            (int(6 * ratio), 6 * ratio, int(self.size.x - 12 * ratio), int(self.size.x - 12 * ratio))
        )
        if self.checked:
            pg.draw.rect(
                self.image, (0, 0, 0),
                (int(12 * ratio), int(12 * ratio), self.size.x - int(24 * ratio), self.size.x - int(24 * ratio))
            )

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, self.size, event.pos):
                self.to_display = not self.hovered
                self.hovered = True
            else:
                self.to_display = self.hovered
                self.hovered = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.engaged and self.hovered:
            self.engaged = False
            self.to_display = True
            self.checked = not self.checked
            self.command(self.checked)

class Slider(Widget):
    def __init__(self, parent, value, on_change):
        super().__init__(parent)
        self.value = value
        self.on_change = on_change

    def display(self):
        ratio = self.parent.parent.ratio
        pg.draw.line(self.parent.surface, (50, 50, 50),
                    self.pos.as_tuple(),
                    (self.pos.x + (self.size.x * self.value) // 1000, self.pos.y),
                    self.size.y)
        pg.draw.line(self.parent.surface, (150, 150, 150),
                    (self.pos.x + (self.size.x * self.value) // 1000, self.pos.y),
                    (self.pos.x + self.size.x, self.pos.y),
                    self.size.y)
        pg.draw.circle(self.parent.surface, (50, 50, 50), (self.pos.x + (self.size.x * self.value) // 1000, self.pos.y), int(25 * ratio))
        self.to_display = False

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION and self.engaged:
            if event.pos[0] <= self.pos.x:
                self.value = 0
            elif event.pos[0] >= self.pos.x + self.size.x:
                self.value = 1000
            else:
                self.value = int(((event.pos[0] - self.pos.x) / self.size.x) * 1000)
            self.on_change(self.value)
            self.to_display = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            ratio = self.parent.parent.ratio
            if is_in(event.pos, (48 * ratio, 48 * ratio), (self.pos.x + (self.size.x * self.value) // 1000 + 24 * ratio, self.pos.y + 24 * ratio)):
                self.engaged = True
        elif event.type == pg.MOUSEBUTTONUP and self.engaged:
            self.engaged = False

class KeyBinder(Widget):
    KEYBINDS = { 0 : '...', 27 : 'Esc', 178 : '²', 49 : '1', 50 : '2', 51 : '3', 52 : '4', 53 : '5', 54 : '6', 55 : '7', 56 : '8', 57 : '9', 48 : '0', 41 : ')', 61 : '=', 8 : 'Backspace', 9 : 'Tab', 97 : 'a', 122 : 'z', 101 : 'e', 114 : 'r', 116 : 't', 121 : 'y', 117 : 'u', 105 : 'i', 111 : 'o', 112 : 'p', 94 : '^', 36 : '$', 13 : 'Enter', 1073741881 : 'C.Lock', 113 : 'q', 115 : 's', 100 : 'd', 102 : 'f', 103 : 'g', 104 : 'h', 106 : 'j', 107 : 'k', 108 : 'l', 109 : 'm', 249 : '%', 42 : 'µ', 1073742049 : 'L Shift', 60 : '<', 119 : 'w', 120 : 'x', 99 : 'c', 118 : 'v', 98 : 'b', 110 : 'n', 44 : ',', 59 : ';', 58 : ':', 33 : '!', 1073742053 : 'R Shift', 1073742048 : 'L Ctrl', 1073742050 : 'L Alt', 32 : 'Space', 1073742054 : 'Fn', 1073742052 : 'R Ctrl', 1073741904 : 'Left', 1073741906 : 'Up', 1073741903 : 'Right', 1073741905 : 'Down', 127 : 'Suppr', 1073741897 : 'Ins', 1073741898 : 'Start', 1073741901 : 'End', 1073741902 : 'Pg. Down', 1073741899 : 'Pg. Up', 1073741922 : 'Keypad 0', 1073741923 : 'Keypad .', 1073741912 : 'Keypad Enter', 1073741913 : 'Keypad 1', 1073741914 : 'Keypad 2', 1073741915 : 'Keypad 3', 1073741916 : 'Keypad 4', 1073741917 : 'Keypad 5', 1073741918 : 'Keypad 6', 1073741911 : 'Keypad +', 1073741919 : 'Keypad 7', 1073741920 : 'Keypad 8', 1073741921 : 'Keypad 9', 1073741908 : 'Keypad /', 1073741909 : 'Keypad *', 1073741910 : 'Keypad -' }

    def __init__(self, parent, key):
        super().__init__(parent)
        self.key = key
        self.awaiting = False

    def update(self):
        self.image = pg.Surface(self.size.as_tuple())
        if self.hovered:
            self.image.fill((200, 200, 200))
        else:
            self.image.fill((255, 255, 255))

        txt = self.parent.font.render(KeyBinder.KEYBINDS[self.key], True, (0, 0, 0))
        size = txt.get_size()
        self.image.blit(txt, ((self.size.x - size[0]) // 2, 0))

    def display(self):
        self.update() # Pas opti
        self.parent.surface.blit(self.image, self.pos.as_tuple())
        self.to_display = False

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            if is_in(self.pos, self.size, event.pos):
                self.to_display = not self.hovered
                self.hovered = True
            else:
                self.to_display = self.hovered
                self.hovered = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.engaged = self.hovered

        elif self.engaged and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.awaiting = True
            self.engaged = False
            self.key = 0
            self.to_display = True

        elif self.awaiting and event.type == pg.KEYDOWN:
            if event.key in KeyBinder.KEYBINDS:
                self.key = event.key
                self.to_display = True
                self.awaiting = False
