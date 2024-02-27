class Bullet:
  def __int__(self,x,y,sprite,damage,speed):
      self.x = x
      self.y = y
      self.sprite = sprite
      self.damage = damage
      self.speed = speed
      self.Hitbox = None

    def move(self, x, y):
        pass
