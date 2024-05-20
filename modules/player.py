import random
import time
from modules.item import HealthPack, Weapon, Item


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.health = 100
        self.resources = {"Medicinal Plant": 0, "Metal": 0, "Crystal": 0}
        self.inventory = {"Health Pack": 0, "Laser Gun": 0}
        self.bag_resources = {"Medicinal Plant": 0, "Metal": 0, "Crystal": 0}
        self.bag_inventory = {"Health Pack": 0, "Laser Gun": 0}
        self.last_heal_time = None

    def is_alive(self):
        return self.health > 0

    def explore(self, planet):
        is_planet_cleared = self.encounter(planet.content)
        if is_planet_cleared:
            self.collect_resource(planet.resource)

    def collect_resource(self, resource):
        self.bag_resources[resource.type] += resource.value
        print(
            f"Collected {resource.value} units of {resource.type}! Total {resource.type}: {self.resources[resource.type]}"
        )

    def encounter(self, alien):
        print(f"A hostile {alien.species} appears!")
        while self.health > 0 and alien.health > 0:
            action = input(
                "Do you want to (A)ttack, (R)etreat, or (U)se Item? "
            ).lower()
            if action == "a":
                self.attack(alien)
                if alien.health > 0:
                    alien.attack(self)
            elif action == "r":
                print("You retreated to your spaceship!")
                break
            elif action == "u":
                self.game.item_menu()  # Use the Game instance reference to call crafting_menu
            else:
                print("Invalid action.")
        if self.health <= 0:
            print("You have been slain by the alien!")
            self.drop_item()
            return False
        elif alien.health <= 0:
            print(f"You have defeated the {alien.species}!")
            return True

    def attack(self, alien):
        damage = random.randint(10, 20)
        alien.health -= damage
        if alien.health > 0:
            print(
                f"You dealt {damage} damage to the {alien.species}. Its health is now {alien.health}."
            )

    def craft_item(self, item_class):
        item = item_class()
        if item.can_craft(self.resources):
            item.craft(self.resources)
            self.bag_inventory[item.name] += 1
            print(f"Crafted a {item.name}!")
        else:
            print(f"Insufficient resources to craft {item.name}.")

    def heal(self):
        current_time = time.time()
        cooldown = 300  # 300 seconds = 5 minutes

        if (
            self.last_heal_time is None
            or (current_time - self.last_heal_time) >= cooldown
        ):
            self.health = 100
            self.last_heal_time = current_time
            print("Healed to full health!")
        else:
            remaining_time = cooldown - (current_time - self.last_heal_time)
            print(f"Cannot heal yet. Please wait {remaining_time:.1f} more seconds.")

    def use_item(self, item_class: Item):
        item = item_class()
        if item.can_use(self.inventory):
            item.use(self.inventory)

    def drop_item(self):
        for key in self.bag_resources:
            self.bag_resources[key] = 0
        for key in self.bag_inventory:
            self.bag_inventory[key] = 0
        print("You have dropped all your items")

    def store_item(self):
        for key in self.bag_resources:
            self.resources[key] += self.bag_resources[key]
            self.bag_resources[key] = 0

        for key in self.bag_inventory:
            self.inventory[key] += self.bag_inventory[key]
            self.bag_inventory[key] = 0
