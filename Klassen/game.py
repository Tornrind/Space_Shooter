import tkinter as windowcreator

class Game:
    def __init__(self, spielername, score=0, leben=3, level=1, window):
        self.spielername = spielername
        self.score = score
        self.leben = leben
        self.level = level
        self.window = window
        self.Bullet = None
        self.Spaceship = None
        self.Asteroid = None
        self.Powerup = None
    def start(self):
        pass

    def create_asteroid (self, Asteroid):
        pass
    def process_input(self):
        pass

    def handle_collision(self):
        if self.leben > 0:
            self.leben -= 1
            print("LEBEN GENOMMEN")
        else:
            print("LEBEN GENOMMEN! EHRE GENOMMEN! DU HAST VERLOREN!")

    def render(self):
        pass

    def anzeigen(self):
        print(f"Spieler: {self.spielername}")
        print(f"Punkte: {self.score}")
        print(f"Leben: {self.leben}")
        print(f"Level: {self.level}")

    # create window

    window = windowcreator.Tk()
    window.title = ("Space Shooter")


    def punkte_erhoehen(self, score):
        self.score += score



