# Write a class to hold player information, e.g. what room they are in
# currently.

# needs name, current_room attributes

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Player name: {self.name}, Current room: {self.current_room}"
