import random
from modules.crafting import HealthPack, Weapon


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game  # Store the reference to the Game instance
        self.health = 100
        self.resources = {'Medicinal Plant': 0, 'Metal': 0, 'Crystal': 0}
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def explore(self, planet):
        self.collect_resource(planet.resource)

    def collect_resource(self, resource):
        self.resources[resource.type] += resource.value
        print(f"Collected {resource.value} units of {resource.type}! Total {resource.type}: {self.resources[resource.type]}")

    def encounter(self, alien):
        print(f"A hostile {alien.species} appears!")
        while self.health > 0 and alien.health > 0:
            action = input("Do you want to (A)ttack, (R)etreat, or (C)raft? ").lower()
            if action == 'a':
                self.attack(alien)
                if alien.health > 0:
                    alien.attack(self)
            elif action == 'r':
                print("You retreated to your spaceship!")
                break
            elif action == 'c':
                self.game.crafting_menu()  # Use the Game instance reference to call crafting_menu
            else:
                print("Invalid action.")
        if self.health <= 0:
            print("You have been slain by the alien!")
        elif alien.health <= 0:
            print(f"You have defeated the {alien.species}!")

    def attack(self, alien):
        damage = random.randint(10, 20)
        alien.health -= damage
        print(f"You dealt {damage} damage to the {alien.species}. Its health is now {alien.health}.")

    def craft_item(self, item_class):
        item = item_class()
        if item.can_craft(self.resources):
            item.craft(self.resources)
            self.inventory.append(item)
            print(f"Crafted a {item.name}!")
        else:
            print(f"Insufficient resources to craft {item.name}.")

    def heal(self):
        if self.resources['Medicinal Plant'] >= 1:
            self.health = 100
            self.resources['Medicinal Plant'] -= 1
            print("Healed to full health!")
        else:
            print("Insufficient Medicinal Plants to heal.")
