
class Asteroid:

    def __init__(self, x, y, speed, sprite, hp):
        self.x = x
        self.y = y
        self.sprite = sprite
        '''picture implemetation, maybe tkinter'''
        self.speed = speed
        self.hp = hp

    def move(self, y, x):
        self.x = x
        self.y = y
        pass
