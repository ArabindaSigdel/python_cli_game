from resource import Resource
from mob import Martian, Venusian


class Planet:
    def __init__(self, name, description, resource, mob):
        self.name = name
        self.description = description
        self.resource = resource
        self.content = mob


# Example planets
planets = [
    Planet("Mars", "a dusty red planet.", Resource("Metal"), Martian()),
    Planet("Venus", "a planet with acidic clouds.", Resource("Medicinal Plant"), Venusian()),
    Planet("Jupiter", "a gas giant with raging storms.", Resource("Metal"), Venusian()),
    Planet("Saturn", "a planet with beautiful rings.", Resource("Crystal"), Martian()),
    Planet("Neptune", "a cold, blue planet.", Resource("Crystal"), Martian()),
    Planet("Uranus", "an ice giant.", Resource("Medicinal Plant"), Martian()),
]
