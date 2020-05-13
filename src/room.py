# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, type, description):
        self.type = type
        self.description = description

    def __str__(self):
        print(self.description)
