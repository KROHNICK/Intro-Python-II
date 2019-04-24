# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room
from item import Lightsource


class Player:
    def __init__(self, name, inventory, current_room):
        self.name = name
        self.inventory = []
        self.current_room = current_room.name

    def pickup_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def actions(self, action, location):
        item = False
        for i in location.items:
            if(action[0] == "get" or "take" and i.name == action[1]):
                item = True
                self.inventory.append(action[1])
                location.remove_item(i)
                print(f"Picked up {action[1]}.")
        for i in self.inventory:
            if(action[0] == "drop" and i == action[1]):
                item = True
                self.inventory.remove(action[1])
                location.add_item(i)
                if (i == "torch"):
                    print("Goodbye light.")
                print(f"Dropped {action[1]}.")
        if(item == False):
            print("Item not found.")

    def print_inventory(self):
        for i in self.inventory:
            print(i.name)
