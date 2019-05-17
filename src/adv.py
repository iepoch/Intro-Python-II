from room import Room
from player import Player
import textwrap
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside The Umbrella Manson",
                     '''*(View of an evil-looking dog-face, complete with growl noises... View
switches to Jill and Chris, scouting together... View switches to Joseph,
scouting alone. He raises his hand and tries to grab his team's attention.)*
                        '''),

    'inside':    Room("Foyer", """As you make it into the foyer you see stairs in front of you a door to the east and a door to the west of you.
                      And a you hear shots ring out from the west of you.
                      """),

    'main_hall': Room("Main Hall", """You step futher into the main hall and see the winding stair case up to another level of the manson. You start up the stairs when
                      you hear even more shots ring out from the west of your location."""),

    'dinning':   Room("Enter the Dinning Room", """Two deep oak french door open with a slight creak to them as you walk into a very large Dinning Room.
You notice that their are some pictures on the wall with a very long dinning table. At the end you see a fireplace. To the East you see another door"""),

    'stairs': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'room1': Room("Gallery", """Gallery of all the fine arts with a statue at the very end. When you hear a sound of a dog growling in the back. You begin to step back away from the hound"""),
}

items = {
    'ink_ribbon': Item('room1', 'Ink Ribbon', "This will help you send a message to your partner on your current location"),
    'green_herb': Item('dinning', 'Green Herb', "Help heal your wounds")

}
# Link rooms together

room['outside'].n_to = room['inside']
room['inside'].s_to = room['main_hall']
room['room1'].w_to = room['dinning']
room['inside'].e_to = room['room1']
room['dinning'].n_to = room['main_hall']
room['stairs'].s_to = room['outside']
room['main_hall'].e_to = room['stairs']
room['stairs'].w_to = room['room1']

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

    # * Prints the current room name
  
    print('\nCurrent location: ', player.cur_room.name)
# * Prints the current description (the textwrap module might be useful here).
# Print Items
    for item in items:
        if items[item].loc == player.cur_room:
            print(
                f'\nThere is a {items[item].name}, a {items[item].description}\n')
    # Where is the player currently
    print(textwrap.fill(player.cur_room.description))
# * Waits for user input and decides what to do.

    direction = input(
        "\n Which direction do you want to go? (n,s,e,w) or q for quit:").lower().strip()
    cls()
# If the user enters a cardinal direction, attempt to move to the room there.
    if direction == 'n':

        try:
            player.cur_room = player.cur_room.n_to
            print(player.cur_room.name)

        except AttributeError:
            print("\nDoor is locked you can not get out of this place!")

    elif direction == 's':

        try:
            player.cur_room = player.cur_room.s_to

        except AttributeError:
            print("\nYou already gone too far south, and you can't go any futher")

    elif direction == 'e':

        try:
            player.cur_room = player.cur_room.e_to
            print(player.cur_room.inventory)
        except AttributeError:
            print("\nYou are already in the east")

    elif direction == 'w':
        cls()
        try:
            player.cur_room = player.cur_room.w_to
            print(player.cur_room.inventory)
        except AttributeError:
            print(
                "\nYou can't go any further and you see a dead body laying in front of you.")

    elif direction == 'q':
        print("\nThanks for playing")
        break
    else:
        continue

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
