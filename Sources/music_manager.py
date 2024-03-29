import pygame as pg
from utils import get_asset

def play_menu_theme():
    pg.mixer.music.stop()
    pg.mixer.music.load(get_asset('Sounds/menu.mp3'))
    pg.mixer.music.play(-1)

def play_game_theme():
    pg.mixer.music.stop()
    pg.mixer.music.load(get_asset('Sounds/theme.mp3'))
    pg.mixer.music.play(-1)

def stop_music():
    pg.mixer.music.stop()

def change_volume(volume):
    pg.mixer.music.set_volume(volume / 1000)
