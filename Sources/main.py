from menu import Menu
import sys

try:
    import pygame as pg
except:
    print("Pygame not found. Please install it with 'pip install pygame'")
    sys.exit(1)

Menu().main()
pg.quit()
