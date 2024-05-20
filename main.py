import random


class Game:
    def __init__(self):
        self.galaxy = Galaxy()
        self.player = Player("Explorer")
        self.current_planet_index = 0

    def start(self):
        print("Welcome to Galactic Explorer: Advanced!")
        while self.current_planet_index < len(self.galaxy.planets):
            print(f"\nArriving at Planet {self.current_planet_index + 1}")
            self.explore_planet(self.galaxy.planets[self.current_planet_index])
            if self.player.is_alive():
                self.current_planet_index += 1
            else:
                print("You have perished in space! Game Over.")
                break
        if self.player.is_alive():
            print("Congratulations! You have explored the entire galaxy!")

    def explore_planet(self, planet):
        print(f"\nExploring {planet.name}: {planet.description}")
        self.player.explore(planet)
        if isinstance(planet.content, Alien):
            self.player.encounter(planet.content)
        elif isinstance(planet.content, Resource):
            self.player.collect_resource(planet.content)

    def crafting_menu(self):
        print("\nCrafting Menu:")
        print("1. Health Pack (Requires 2 Medicinal Plants, 1 Metal)")
        print("2. Laser Gun (Requires 2 Metal, 1 Crystal)")
        choice = input("Choose an item to craft (1 or 2): ")
        if choice == '1':
            self.player.craft_item(HealthPack)
        elif choice == '2':
            self.player.craft_item(Weapon)
        else:
            print("Invalid choice.")


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.resources = {'Medicinal Plant': 0, 'Metal': 0, 'Crystal': 0}
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def explore(self, planet):
        if isinstance(planet.content, Resource):
            self.collect_resource(planet.content)

    def collect_resource(self, resource):
        self.resources[resource.type] += resource.value
        print(
            f"Collected {resource.value} units of {resource.type}! Total {resource.type}: {self.resources[resource.type]}")

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
                game.crafting_menu()
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


class Resource:
    def __init__(self, resource_type, value):
        self.type = resource_type
        self.value = value


class Planet:
    def __init__(self, name, description, content):
        self.name = name
        self.description = description
        self.content = content


class Galaxy:
    def __init__(self):
        self.planets = self.create_galaxy()

    def create_galaxy(self):
        planets = []
        planets.append(Planet("Mars", "a dusty red planet.", Martian()))
        planets.append(Planet("Venus", "a planet with acidic clouds.", Venusian()))
        planets.append(Planet("Jupiter", "a gas giant with raging storms.", Resource("Metal", 100)))
        planets.append(Planet("Saturn", "a planet with beautiful rings.", Resource("Crystal", 150)))
        planets.append(Planet("Neptune", "a cold, blue planet.", Martian()))
        planets.append(Planet("Uranus", "an ice giant.", Resource("Medicinal Plant", 120)))
        return planets


class Item:
    def __init__(self, name):
        self.name = name

    def can_craft(self, resources):
        raise NotImplementedError

    def craft(self, resources):
        raise NotImplementedError


class HealthPack(Item):
    def __init__(self):
        super().__init__("Health Pack")

    def can_craft(self, resources):
        return resources['Medicinal Plant'] >= 2 and resources['Metal'] >= 1

    def craft(self, resources):
        resources['Medicinal Plant'] -= 2
        resources['Metal'] -= 1

    def use(self, player):
        player.health += 50
        if player.health > 100:
            player.health = 100
        print(f"Used a Health Pack! Health is now {player.health}")


class Weapon(Item):
    def __init__(self):
        super().__init__("Laser Gun")

    def can_craft(self, resources):
        return resources['Metal'] >= 2 and resources['Crystal'] >= 1

    def craft(self, resources):
        resources['Metal'] -= 2
        resources['Crystal'] -= 1

    def attack(self, alien):
        damage = random.randint(20, 40)
        alien.health -= damage
        print(f"Laser Gun dealt {damage} damage to the {alien.species}. Its health is now {alien.health}.")


if __name__ == "__main__":
    game = Game()
    game.start()
