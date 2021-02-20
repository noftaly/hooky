import pygame as pg
from vector import Vector


class Level:
    CELL_SIZE = 64
    def __init__(self, game, number_level):
        self.game = game
        self.level_array = []
        self.read_level(number_level)

    def display(self):
        pos = self.game.player.pos
        backgroundLeftOffset = round(Vector(pos.x // 64 - 15, pos.y // 64 - 8))
        # We prevent leftBackgroundOffset to be below 0
        backgroundLeftOffset.x = max([backgroundLeftOffset.x, 0])
        backgroundLeftOffset.y = max([backgroundLeftOffset.y, 0])

        rngX = 31
        if backgroundLeftOffset.x + 31 >= len(self.level_array[0]):
            rngX = len(self.level_array[0]) - backgroundLeftOffset.x

        rngY = 18
        if backgroundLeftOffset.y + 18 >= len(self.level_array):
            rngY = len(self.level_array) - backgroundLeftOffset.y

        for row in range(rngX): # roundup(1920 / 64) + 1
            for col in range(rngY): # roundup(1080/64) + 1
                # (row index + X offset according to the player) * the cell cize + center of screen - the X position of the player
                x = (row + backgroundLeftOffset.x) * self.CELL_SIZE + self.game.half_size[0] - pos.x
                # (column index +Y offset according to the player) * the cell cize + center of screen - the Y position of the player
                y = (col + backgroundLeftOffset.y) * self.CELL_SIZE + self.game.half_size[1] - pos.y

                # Dirt
                if self.level_array[backgroundLeftOffset.y + col][backgroundLeftOffset.x + row] == 1:
                    pg.draw.rect(self.game.surface, (101, 67, 33), (x, y, self.CELL_SIZE, self.CELL_SIZE))
                # Sky
                elif self.level_array[backgroundLeftOffset.y + col][backgroundLeftOffset.x + row] == 0:
                    pg.draw.rect(self.game.surface, (119, 181, 254), (x, y, self.CELL_SIZE, self.CELL_SIZE))

    def update(self):
        pass

    def read_level(self, number_level):
        self.level_array = []
        # r+t: read as text file
        with open("./Levels/level_" + str(number_level) + ".lvl", mode='r+t') as levelFile:
            for (i, line) in enumerate(levelFile):
                if line[-1] == '\n':
                    line = line[:-1]
                if i == 0:
                    # Transforms a string "x,y" into a tuple (x,y), with x,y as integers
                    self.spawn = Vector(*map(int, line.split(',')))
                else:
                    # Adds the row converted into integers to level_array
                    self.level_array.append(list(map(int, line)))
