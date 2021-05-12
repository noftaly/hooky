from menu import Menu
#from game import Game

try:
    import pygame as pg
except:
    print("Pygame not found. Please install it with 'pip install pygame'")
    exit(1)

#Game(0).main()
Menu().main()
pg.quit()