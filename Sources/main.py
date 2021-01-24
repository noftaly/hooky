"""
Initialisations, instalation des librairies
"""

import os
#from menu import Menu
from game import Game

try:
    import pygame as pg
except:
    system("pip install pygame")
    pass

pg.init()
pg.display.set_mode((1000,1000))

Game(0).main()
#Menu().main()