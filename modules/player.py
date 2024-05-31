# player.py
from modules.item import HealthPack, Weapon

class Player:
    def __init__(self, name, game):
        self.name = name
        self.health = 100
        self.inventory = {"Health Pack": 5, "Laser Gun": 3}
        self.storage = []
        self.resources = {'Medicinal Plant': 0, 'Metal': 0, 'Crystal': 0}
        self.game = game

    def explore(self, planet):
        # Explore the planet (handled in game.py)
        pass

    def heal(self):
        if self.inventory["Health Pack"] > 0:
            health_pack = HealthPack()
            health_pack.use(self, self.inventory)
        else:
            print("No Health Packs available.")

    def craft_item(self, item_class):
        item = item_class()
        if item.can_craft(self.resources):
            item.craft(self.resources)
            self.inventory[item.name] += 1
            print(f"{item.name} crafted.")
        else:
            print(f"Insufficient resources to craft {item.name}.")

    def view_all_items(self):
        if any(self.inventory.values()):
            print("Inventory:")
            for item, quantity in self.inventory.items():
                if quantity > 0:
                    print(f"- {item}: {quantity}")
        else:
            print("Inventory is empty.")

    def use_item(self, item_class, target=None):
        item = item_class()
        if item.can_use(self.inventory):
            item.use(target, self.inventory)
        else:
            print(f"No {item.name} available.")

    def collect(self, resource):
        if resource.type in self.resources:
            self.resources[resource.type] += resource.value
            print(f"Collected {resource.value} {resource.type}(s).")
        else:
            print(f"Unknown resource: {resource.type}")

    def store_item(self):
        if not any(self.inventory.values()):
            print("No items to store.")
            return

        while True:
            print("Items in inventory:")
            for i, (item, quantity) in enumerate(self.inventory.items()):
                if quantity > 0:
                    print(f"{i + 1}. {item}: {quantity}")

            choice = input("Choose an item to store (or 'q' to quit): ").lower()
            if choice == 'q':
                break

            try:
                choice = int(choice) - 1
                item_name = list(self.inventory.keys())[choice]
                if self.inventory[item_name] > 0:
                    self.inventory[item_name] -= 1
                    self.storage.append(item_name)
                    print(f"Stored {item_name}.")
                else:
                    print("Invalid choice. Please try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number.")

    def view_storage(self):
        if self.storage:
            print("Storage:")
            for item in self.storage:
                print(f"- {item}")
        else:
            print("Storage is empty.")
