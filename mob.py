import random


class Alien:
    def __init__(self, species, health):
        self.species = species
        self.health = health

    def attack(self, player):
        damage = random.randint(10, 25)
        player.health -= damage
        print(f"The {self.species} dealt {damage} damage to you. Your health is now {player.health}.")


class Martian(Alien):
    def __init__(self):
        super().__init__("Martian", random.randint(40, 60))


class Venusian(Alien):
    def __init__(self):
        super().__init__("Venusian", random.randint(50, 70))
