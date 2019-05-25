# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:

    def __init__(self, name, description, inventory=[]):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        output = "You have open the door into the..." + str(self.name)
        output += "\n" + self.description
        output += "\n" + "You noticed a glint of something near the fireplace, you found:"

        # Print Items
        for i in self.inventory:
            output += f'\n{i.name}, {i.description}'
        return output
