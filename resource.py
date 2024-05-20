import random


class Resource:
    def __init__(self, resource_type):
        self.type = resource_type
        self.value = random.randint(0, 5)
