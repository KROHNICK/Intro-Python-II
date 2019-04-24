class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self, picked_up):
        self.picked_up = picked_up

    def on_drop(self, dropped):
        self.dropped = dropped


class Treasure(Item):
    def __init__(self, name, descr, value):
        super().__init__(name, descr)
        self.value = value


class Lightsource(Item):
    def __init__(self, name, descr):
        super().__init__(name, descr)
