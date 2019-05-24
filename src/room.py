# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:

    def __init__(self, name, description, inventory=[]):
        self.name = name
        self.description = description
        self.inventory = inventory
        
    def __str__(self):
        output = "You are now in..." + str(self.name)
        output += "\n" + self.description
        output += "\n" + "Items:"
        
            # Print Items
        for i in self.inventory:
            output += '\n' + i.name + "," + i.description
        return output