#File for fancy smanshy items

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print("You have picked up " + self.name)

    def __str__(self):
        print(self.name + ": " + self.description)
