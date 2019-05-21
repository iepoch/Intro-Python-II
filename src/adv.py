from room import Room
from player import Player
import textwrap
# Declare all the rooms

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
room['foyer'].s_to = room['narrow']
room['narrow'].e_to = room['overlook']
room['overlook'].w_to = room['treasure']
room['treasure'].n_to = room['overlook']
room['overlook'].s_to = room['outside']
room['treasure'].e_to = room['foyer']
room['foyer'].w_to = room['narrow']

#
# Main
#


def cls():
    print('\n' * 100)


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
# While loop for Adventure game
while True:

    # Where is the player currently
    # * Prints the current room name
    cur_room = player.cur_room
    print('\nCurrent location: ', cur_room.name)
# * Prints the current description (the textwrap module might be useful here).

    print(textwrap.fill(cur_room.description))
# * Waits for user input and decides what to do.

    direction = input(
        "\n Which direction do you want to go? (n,s,e,w) or q for quit:").lower().strip()
    cls()
# If the user enters a cardinal direction, attempt to move to the room there.
    if direction == 'n':

        try:
            player.cur_room = cur_room.n_to
            print(cur_room.name, cur_room.description)
        except AttributeError:
            print("\nYou already North of the wall")

    elif direction == 's':

        try:
            player.cur_room = cur_room.s_to
            print(cur_room.name, cur_room.description)
        except AttributeError:
            print("\nYou already gone too far south, and you can't go any futher")

    elif direction == 'e':

        try:
            player.cur_room = cur_room.e_to
            print(cur_room.description)
        except AttributeError:
            print("\nYou are already in the east")

    elif direction == 'w':
        cls()
        try:
            player.cur_room = cur_room.w_to
            print(cur_room.description)
        except AttributeError:
            print("\nWestros is to the south")

    elif direction == 'q':
        print("\nThanks for playing")
        break
    else:
        continue

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
