# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Item name: {self.name}, Item description: {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")