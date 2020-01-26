from sprite import Sprite


class Laser(Sprite):
    def __init__(self, x, y, size_x, size_y):
        super(Laser, self).__init__(x, y, size_x, size_y)
        self.ascii_x = 5
        self.ascii_y = 1
        self.ascii = ['-----']
        self.maker()
        self.move()