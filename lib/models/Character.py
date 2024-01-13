from models.__init__ import CURSOR, CONN


class Character:
    def __init__(self, name, hp, level = 1, xp = 0):
        self.name = name
        self.hp = hp
        self.level = level
        self.xp = xp

        