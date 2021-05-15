import sys
from menu import Menu

try:
    import pygame as pg
except ModuleNotFoundError:
    print("Pygame not found. Please install it with 'pip install pygame'")
    sys.exit(1)

Menu().main()
pg.quit()
