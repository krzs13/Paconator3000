from sprite import Sprite


class Paco(Sprite):
    def __init__(self, x, y, size_x, size_y):
        super(Paco, self).__init__(x, y, size_x, size_y)
        self.ascii_x = 15
        self.ascii_y = 5
        self.ascii = ['    /"\__      ',
                      '   (    @\____ ',
                      '  /           O',
                      ' /    (______/ ',
                      '/_____/     U  ']
        self.maker()