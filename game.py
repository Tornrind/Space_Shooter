class Game:
    def __init__(self, spielername, punkte=0, leben=3, level=1):
        self.spielername = spielername
        self.punkte = punkte
        self.leben = leben
        self.level = level

    def anzeigen(self):
        print(f"Spieler: {self.spielername}")
        print(f"Punkte: {self.punkte}")
        print(f"Leben: {self.leben}")
        print(f"Level: {self.level}")

    def punkte_erhoehen(self, punkte):
        self.punkte += punkte

    def leben_verringern(self):
        if self.leben > 0:
            self.leben -= 1
            print("Leben verloren!")
        else:
            print("Spiel vorbei! Keine Leben mehr.")

    def level_erhoehen(self):
        self.level += 1
        print(f"Herzlichen Glückwunsch! Du bist jetzt auf Level {self.level}.")