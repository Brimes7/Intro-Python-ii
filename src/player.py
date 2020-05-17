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
        else:
            print("That item isn't at your disposal.")

    def take(self, item_name):
        self.grab(item_name)

    def drop(self, item_name):
        for itm in self.items:
            #Checking if the item is what we want
            if itm.name == item_name:
                self.items.remove(itm)
                #removed from player and added to the room
                self.room.add_item(itm)

    def inventory(self, item_name):
        item = self.room.get_item(item_name)
        if item is not None:
            print("Would you like to check the inventory?")




