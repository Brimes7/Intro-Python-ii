# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        self.room.__str__()

    def grab(self, item_name):
        item = self.room.get_item(item_name)
        if item is not None:
            item.on_take()
            self.items.append(item)

    def take(self, item_name):
        self.grab(item_name)

    def drop(self, item_name):




