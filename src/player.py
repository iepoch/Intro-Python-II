# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, cur_room, inventory=[]):
        self.cur_room = cur_room
        self.inventory = inventory

    def __str__(self):
        return f'Player currently {self.cur_room}'
