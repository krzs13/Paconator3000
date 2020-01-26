import os


class Saver():
    def save(self, record):
        with open('save.txt', 'w') as score:
            score.write(str(record))

    def load(self):
        if os.path.exists('save.txt'):
            content = ''
            with open('save.txt', 'r') as score:
                content = score.readline()

            return content
