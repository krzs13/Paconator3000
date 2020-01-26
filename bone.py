from sprite import Sprite


class Bone(Sprite):
    def __init__(self, x, y, size_x, size_y):
        super(Bone, self).__init__(x, y, size_x, size_y)
        self.ascii_x = 5
        self.ascii_y = 1
        self.ascii = ['8===8']
        self.maker()
        self.move()

