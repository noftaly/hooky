import pygame as pg
from utils import get_asset

def play_menu_theme():
    pg.mixer.music.stop()
    pg.mixer.music.load(get_asset('menu.mp3'))
    pg.mixer.music.play(-1)

def play_game_theme():
    pg.mixer.music.stop()
    pg.mixer.music.load(get_asset('theme.mp3'))
    pg.mixer.music.play(-1)

def stop_music():
    pg.mixer.music.stop()
