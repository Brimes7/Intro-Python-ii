import sys

from room import Room
from player import Player
from item import Item


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room .
player = Player("dum dum", room['outside'])

room['outside'].add_item(Item("sword", "A shiny double edged sword"))
room['foyer'].add_item(Item("FlameThrower", "Powerful funnel of fire"))
room['overlook'].add_item(Item("JetPack", "Light weight battery powered flying mechanism"))
room["narrow"].add_item(Item("Shield", "Strong defense made of steel"))
room["treasure"].add_item(Item("jewels", "Rubies and emeralds"))


# Write a loop that:
#
# * Prints the current room name
command = ""
while True:
    player.__str__()
    command = input("Enter the direction using cardinal abbreviations(i.e - N, S, E, W. Or Q when you give up, if along the way you find treasure - use grab or drop as you see fit: ")
    #looking for every space
    command = command.split(" ")
    if command.__len__() is 1:

        new_room = getattr(player.room, command[0].lower() + "_to", None)
        if new_room:
            player.room = new_room
        elif command is "q" or command is "Q":
            print("You broke the game. ")
            sys.exit(1)
        elif command is "i" or command is "inventory":
            print("In your inventory you have acquired: " + player.room)
        else:
            print("You suck, try again. ")
    elif len(command) is 2:
        function = getattr(player, command[0].lower(), None)
        if function:
            function(command[1])
    # elif command is "i":
    #     print("In your inventory you have acquired: " + player.inventory)

    else:
        print("length is 2")

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
