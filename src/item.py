
class Item:

    def __init__(self, loc, name, description):
        self.loc = loc
        self.name = name
        self.description = description
    def __str__(self):
        return f'These Items are here {self.name}'