from abc import ABC
from point import Point


class Sprite(ABC):
    def __init__(self, x, y, size_x, size_y):
        self.x = x  # initial position on a map
        self.y = y
        self.size_x = size_x  # size of a map
        self.size_y = size_y
        self.sprite = []  # sprite that could be set on a map
        self.direction = Point(0, 0)
        # ------ overwrite stuff below in child class ------
        self.ascii_x = 0  # size of an ascii character
        self.ascii_y = 0
        self.ascii = []  # ascii character
        self.maker()

    def maker(self):
        for y in range(self.ascii_y):
            self.sprite.append([])
            for x in range(self.ascii_x):
                self.sprite[y].append(Point(x + self.x, y + self.y, self.ascii[y][x]))

    def move(self):  # if sprite in map borders then move
        if self.sprite[0][0].x + self.direction.x > 0 \
                and self.sprite[self.ascii_y - 1][self.ascii_x - 1].x + self.direction.x < self.size_x + 1:
            if self.sprite[0][0].y + self.direction.y > 0 \
                    and self.sprite[self.ascii_y - 1][self.ascii_x - 1].y + self.direction.y < self.size_y + 1:
                for y in range(self.ascii_y):
                    for x in range(self.ascii_x):
                        self.sprite[y][x].x += self.direction.x
                        self.sprite[y][x].y += self.direction.y














    """class Paco:
        def __init__(self, x, y, size_x, size_y):
            self.x = x
            self.y = y
            self.size_x = size_x
            self.size_y = size_y
            self.paco_sprite = ['    /"\__      ',
                                '   (    @\____ ',
                                '  /           O',
                                ' /    (______/ ',
                                '/_____/     U  ']
            self.paco = []
            self.maker()
            self.direction = Point(0, 0)

        def maker(self):
            for y in range(5):
                self.paco.append([])
                for x in range(15):
                    self.paco[y].append(Point(self.x + x, self.y + y, self.paco_sprite[y][x]))

        def move(self):
            if self.paco[0][0].x + self.direction.x > 0 and self.paco[4][14].x + self.direction.x < self.size_x + 1\
                    and self.paco[0][0].y + self.direction.y > 0 and self.paco[4][14].y + self.direction.y < self.size_y + 1:
                for y in range(5):
                    for x in range(15):
                        self.paco[y][x].x += self.direction.x
                        self.paco[y][x].y += self.direction.y"""




