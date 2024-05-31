# game.py
from modules.galaxy import Galaxy
from modules.player import Player
from modules.mob import Alien
from modules.item import HealthPack, Weapon
from modules.game_data import GameData
import random


class Game:
    def __init__(self):
        self.galaxy = Galaxy()
        self.player = Player("Explorer", self)
        self.current_planet_index = 0
        self.data_manager = GameData()

    def start(self):
        print("Welcome to Galactic Explorer!")
        loaded_game = self.data_manager.load()
        if loaded_game:
            self.__dict__.update(loaded_game.__dict__)
            print("Loaded saved game.")
        while True:
            self.display_main_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.choose_planet()
            elif choice == "2":
                self.hq_menu()
            elif choice == "3":
                self.data_manager.save(self)
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_main_menu(self):
        print("\n--- Main Menu ---")
        print("1. Explore a planet")
        print("2. Return to HQ")
        print("3. Exit game")

    def choose_planet(self):
        print("\nPlanets in the galaxy:")
        for i, planet in enumerate(self.galaxy.planets):
            print(f"{i + 1}. {planet.name}")
        try:
            choice = int(input("Choose a planet to explore: ")) - 1
            if 0 <= choice < len(self.galaxy.planets):
                self.explore_planet(self.galaxy.planets[choice])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def explore_planet(self, planet):
        if self.player.health > 0:
            print(f"\nExploring {planet.name}: {planet.description}")
            encounter = random.choice(["alien", "resource", "nothing"])
            if encounter == "alien":
                alien = planet.content
                print(f"You encounter an alien: {alien.description}")
                self.combat(alien)
            elif encounter == "resource":
                resource = planet.find_resource()
                print(f"You find a resource: {resource.type} (Value: {resource.value})")
                self.player.collect(resource)
            else:
                print("You find nothing of interest.")
            self.return_to_hq_option()
        else:
            print("Your HP is too low. You cannot explore now!")

    def combat(self, alien):
        while alien.health > 0 and self.player.health > 0:
            self.item_menu(alien)
            alien.attack(self.player)
            if self.player.health <= 0:
                print("You have been defeated!")
                break
            if alien.health <= 0:
                print("You defeated the alien!")
                break

    def hq_menu(self):
        print("\n--- Headquarters ---")
        while True:
            self.display_hq_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.crafting_menu()
            elif choice == "2":
                self.player.heal()
            elif choice == "3":
                self.player.view_all_items()
            elif choice == "4":
                self.player.view_storage()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_hq_menu(self):
        print("1. Craft an item")
        print("2. Heal")
        print("3. View resources")
        print("4. View storage")
        print("5. Exit HQ")

    def crafting_menu(self):
        print("\nCrafting Menu:")
        print("1. Health Pack (Requires 2 Medicinal Plants, 1 Metal)")
        print("2. Laser Gun (Requires 2 Metal, 1 Crystal)")
        choice = input("Choose an item to craft (1 or 2): ")
        if choice == "1":
            self.player.craft_item(HealthPack)
        elif choice == "2":
            self.player.craft_item(Weapon)
        else:
            print("Invalid choice. Please try again.")

    def return_to_hq_option(self):
        while True:
            choice = choice = input("Do you want to return to HQ? (y/n): ").lower()
            if choice == "y":
                self.hq_menu()
                self.player.store_item()
                break
            elif choice == "n":
                break
            else:
                print("Invalid choice. Please try again.")

    def item_menu(self, target):
        print("\nItem Menu: ")
        print("1. Health Pack")
        print("2. Laser Gun")
        choice = input("Choose an item to use: ")
        if choice == "1":
            self.player.use_item(HealthPack, target)
        elif choice == "2":
            self.player.use_item(Weapon, target)
        else:
            print("Invalid choice. Please try again.")
