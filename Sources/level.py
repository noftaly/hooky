"""


"""

class Level:
    def __init__(self,lvl):
        self.readLvl(lvl)
    def readLvl(self,lvl):
        self.lvAr = []
        with open("../Levels/l"+str(lvl)+".lvl",mode='r+t') as levelFile: #lvl is the lvl number, (../Levels/l"+str(lvl)+".lvl") = Levels/l1.lvl, r+t => read as text file
            i = 0
            for line in levelFile:
                if line[-1] == '\n':
                        line = line[:-1]
                if i == 0:
                    self.spn = tuple(map(int,line[1:-1].split(','))) #transforms a string "(x,y)" into a tuple (x,y), with x,y int
                elif line[0] != '(':
                    self.lvAr.append(list(map(int,line))) #adds the row converted into integers to lvAr
                else:
                    pass #on vera pour les objets custom plus tard (objets déplaçables, texte etc.. )
                i += 1