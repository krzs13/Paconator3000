from multiprocessing.dummy import Process, Value
import os
import getch
import time

Wait = lambda: time.sleep(0.035)
ClearConsole = lambda: os.system('cls')
WindowSize = lambda: os.system('mode 135,37')


class GetKey:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None

    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()

    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break

    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
