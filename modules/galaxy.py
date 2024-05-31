# galaxy.py
from modules.planet import planets
import random


class Galaxy:
    def __init__(self):
        self.planets = planets

    def get_random_resource(self):
        return random.choice([planet.resource for planet in self.planets])

    def get_planet(self, index):
        if 0 <= index < len(self.planets):
            return self.planets[index]
        return None
