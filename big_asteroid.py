class Big_Asteroid():
    def __int__(self, x: float, y: float, speed: float, split_probability: float, hp: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.split_probability = split_probability
        self.hp = hp

    def move(self, y: int, x: int):
        self.y += y
        self.x += x
        pass
    def split(self):
        ''' small_asteroid[] '''
        pass
