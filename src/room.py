# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = []

    def __str__(self):
        print("{self.name}, {self.desc}, {self.items}")

    def add_item(self, *args):
        self.items.extend(args)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        for i in self.items:
            print(i.name)
