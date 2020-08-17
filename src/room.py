# Implement a class to hold room information. This should have name and
# description attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.

class Room:
    def __init__(self, room_name, description, items):
        self.room_name = room_name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    #typehint for other devs 
    def get_item(self, item_name: str):
        # Returns the item corresponding to item_name if it exists in the room, otherwise returns None
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None

# typehint... just getting used to it
    def remove_item(self, item: Item):
        self.items.remove(item)


    def __str__(self):
        return f"Room name: {self.room_name}, Room description: {self.description}"