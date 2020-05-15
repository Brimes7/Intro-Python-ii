# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

#prints the type and eventually the items as well

    def __init__(self, type, description):
        self.type = type
        self.description = description
        self.items = []
# prints the description
    def __str__(self):
        print(self.description)
        print("Inside the room you see: ")

        for items in self.items:
            items.__str__()

#work in progress prints the item
    def add_item(self, item):
        self.items.append(item)

    def get_item(self, item_name):
        # finding the item
        for itm in self.items:
            #Checking if the item is what we want
            if itm.name == item_name:
                self.items.remove(itm)
                #returns item to player
                return itm
        return None
