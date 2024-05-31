# mob.py
import random


class Alien:
    def __init__(self, name, description, health, attack_power):
        self.name = name
        self.description = description
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"The {self.name} attacks you for {damage} damage. You have {player.health} HP left.")


class Martian(Alien):
    def __init__(self):
        super().__init__("Martian", "A hostile Martian from Mars.", 50, 10)


class Venusian(Alien):
    def __init__(self):
        super().__init__("Venusian", "A fierce Venusian from Venus.", 60, 12)


# Add more alien classes as needed

# Example of initializing alien classes
martian = Martian()
venusian = Venusian()
