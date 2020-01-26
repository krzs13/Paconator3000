class Map:
    def __init__(self, size_x, size_y, border):
        self.size_x = size_x
        self.size_y = size_y
        self.border = border
        self.map_clean = []
        self.map = []  # use map to set stuff, map_clean is only to clean
        self.maker(self.map_clean)
        self.maker(self.map)

    def maker(self, map_base):
        for y in range(self.size_y + 2):
            map_base.append([])
            if y == 0:
                for x in range(self.size_x + 2):
                    map_base[0].append(self.border)
            elif 0 < y < self.size_y + 1:
                for x in range(self.size_x + 2):
                    if x == 0:
                        map_base[y].append(self.border)
                    elif 0 < x < self.size_x + 1:
                        map_base[y].append(' ')
                    else:
                        map_base[y].append(self.border)
            else:
                for x in range(self.size_x + 2):
                    map_base[y].append(self.border)

    def printer(self):
        buffer = ''
        for y in range(self.size_y + 2):
            buffer += ''.join(self.map[y])
            if y < self.size_y + 1:
                buffer += '\n'
        print(buffer)

    def cleaner(self):
        for y in range(self.size_y + 2):
            for x in range(self.size_x + 2):
                self.map[y][x] = self.map_clean[y][x]

    def set_point(self, x, y, character):
        self.map[y][x] = character
