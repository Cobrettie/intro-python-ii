# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, item_name, description):
        self.item_name = item_name
        self.description = description
    
    def __str__(self):
        return f"Item name: {self.item_name}, Item description: {self.description}"