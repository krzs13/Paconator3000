from abc import ABC
from point import Point


class Logo(ABC):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.logo = []
        self.screen = []
        self.maker()

    def maker(self):
        for y in range(len(self.logo)):
            self.screen.append([])
            for x in range(len(self.logo[y])):
                self.screen[y].append(Point(int((self.size_x - len(self.logo[y])) / 2) + x + 1, int((self.size_y - len(self.logo)) / 2) + y + 1, self.logo[y][x]))


