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
#work in progress prints the item
    def add_item(self, item):
        self.items.append(item)
