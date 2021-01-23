"""


"""

class Level:
    def __init__(self, lvl):
        self.readLvl(lvl)

    def readLvl(self, lvl):
        self.lvAr = []
        # lvl is the lvl number / r+t => read as text file
        with open("./Levels/level_" + str(lvl) + ".lvl", mode='r+t') as levelFile:
            i = 0
            for line in levelFile:
                if line[-1] == '\n':
                    line = line[:-1]
                if i == 0:
                    # Transforms a string "(x,y)" into a tuple (x,y), with x,y int
                    self.spn = tuple(map(int,line[1:-1].split(',')))
                elif line[0] != '(':
                    # Adds the row converted into integers to lvAr
                    self.lvAr.append(list(map(int,line)))
                else:
                    # On vera pour les objets custom plus tard (objets déplaçables, texte etc.. )
                    pass
                i += 1
