import random


class Item:
    def __init__(self, name):
        self.name = name

    def can_craft(self, resources):
        raise NotImplementedError

    def craft(self, resources):
        raise NotImplementedError

    def can_use(self, inventory):
        raise NotImplementedError

    def use(self, inventory):
        raise NotImplementedError


class HealthPack(Item):
    def __init__(self):
        super().__init__("Health Pack")

    def can_craft(self, resources):
        return resources["Medicinal Plant"] >= 2 and resources["Metal"] >= 1

    def craft(self, resources):
        resources["Medicinal Plant"] -= 2
        resources["Metal"] -= 1

    def can_use(self, inventory):
        return inventory["Health Pack"] >= 1

    def use(self, player):
        player.health += 50
        if player.health > 100:
            player.health = 100
        print(f"Used a Health Pack! Health is now {player.health}")


class Weapon(Item):
    def __init__(self):
        super().__init__("Laser Gun")

    def can_craft(self, resources):
        return resources["Metal"] >= 2 and resources["Crystal"] >= 1

    def craft(self, resources):
        resources["Metal"] -= 2
        resources["Crystal"] -= 1

    def can_use(self, inventory):
        return inventory["Laser Gun"] >= 1

    def use(self, alien):
        damage = random.randint(40, 70)
        alien.health -= damage
        print(
            f"Laser Gun dealt {damage} damage to the {alien.species}. Its health is now {alien.health}."
        )
