
class Asteroid:

    def __init__(self, x: float, y: float, speed: float, sprite: str, hp: int):
        self.x = x
        self.y = y
        self.sprite = sprite
        '''picture implemetation, maybe tkinter'''
        self.speed = speed
        self.hp = hp

    def move(self, y: int, x: int):
        self.x = x
        self.y = y

        pass
