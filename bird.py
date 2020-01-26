from sprite import Sprite


class Bird(Sprite):
    def __init__(self, x, y, size_x, size_y):
        super(Bird, self).__init__(x, y, size_x, size_y)
        self.ascii_x = 7
        self.ascii_y = 5
        self.ascii = ['  ,~   ',
                      ' ("v)__',
                      '(/ (``/',
                      ' \__>" ',
                      '  ^^   ']
        self.maker()
        self.move()


