class Creature:
    sanity = 0
    name = ""
    description = ""

    def __init__(self, sanity, name, description):
        self.sanity = sanity
        self.name = name
        self.description = description

    def look(self):
        print(self.description)

class Mfr(Creature):
    damage = 0

    def __init__(self, sanity, name, description, damage):
        self.sanity = sanity
        self.name = name
        self.description = description
        self.damage = damage

    def attack(self, player):
        player.sanity -= self.damage


class Player(Creature):
    def look(self):
        print("My name is " + self.name)
        super().look()


player = Player(100, "RyanB", "I'm a baby duh")
print(player.sanity)
player.look()

jerry = Mfr(-100, "Jerry", "oh it's a blue bird", 10)
jerry.look()
jerry.attack(player)
print(player.sanity)

dulller = Mfr(-1000, "Duller", "FBI OPEN UP", 100)
dulller.attack(player)
print(player.sanity)
