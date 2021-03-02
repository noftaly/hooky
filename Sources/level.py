from block import Block
from utils import get_2d_array
from vector import Vector


class Level:
    def __init__(self, game, number_level):
        self.game = game
        self.level_array = []
        self.read_level(number_level)

    def display(self):
        left_bound = self.game.player.cell.x - self.game.half_size[0] // self.game.CELL_SIZE - 1
        right_bound = self.game.player.cell.x + self.game.half_size[0] // self.game.CELL_SIZE + 2
        top_bound = self.game.player.cell.y - self.game.half_size[1] // self.game.CELL_SIZE - 1
        bottom_bound = self.game.player.cell.y + self.game.half_size[1] // self.game.CELL_SIZE + 1

        # Convert to int and keep it above 0
        left_visible_bound = max([int(left_bound), 0])
        right_visible_bound = max([int(right_bound), 0])
        top_visible_bound = max([int(top_bound), 0])
        bottom_visible_bound = max([int(bottom_bound), 0])

        for row in range(left_visible_bound, right_visible_bound):
            for col in range(top_visible_bound, bottom_visible_bound):
                cell = get_2d_array(self.level_array, row, col)
                if cell:
                    cell.display()

    def update(self):
        pass

    def read_level(self, number_level):
        self.level_array = []
        # r+t: read as text file
        with open("./Levels/level_" + str(number_level) + ".lvl", mode='r+t') as levelFile:
            for (row, line) in enumerate(levelFile):
                if line[-1] == '\n':
                    line = line[:-1]
                if row == 0:
                    # Transforms a string "x,y" into a tuple (x,y), with x,y as integers
                    self.spawn = Vector(*map(int, line.split(',')))
                else:
                    # Initialize the empty row
                    self.level_array.append([])
                    # Create a block and add it to the row
                    for (col, block) in enumerate(line):
                        new_block = Block(Vector(col, row - 1), self.game, int(block))
                        self.level_array[row - 1].append(new_block)
            print(self.level_array)
