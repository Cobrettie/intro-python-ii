from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ['dirt', 'rock', 'shrub', 'insect']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['rusty sword', 'empty chalice', 'shattered armor']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['skeleton', 'armor', 'sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['chains', 'bones']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['salvation in Jesus Christ']),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main

# Make a new player object that is currently in the 'outside' room.
Cobra = Player('Cobra', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w', or 'q' to quit)")

    if user_input == "q":
        break

    if user_input == "n":
        if Cobra.current_room.n_to:
            # change current room
            Cobra.current_room = Cobra.current_room.n_to
            print(f"{Cobra.name} moved north \n")
            print(f"{Cobra.current_room.room_name}\n")
            print(f"{Cobra.current_room.description}\n")
            view_items = input("View this rooms items? y, n\n")
            if view_items == 'y':
                print(Cobra.current_room.items)
            if view_items == 'n':
                print("On your way then...\n")
        else:
            print("Can not move there, no room to go to\n")

    if user_input == "s":
        if Cobra.current_room.s_to:
            Cobra.current_room = Cobra.current_room.s_to
            print("player moved south \n")
            print("Player 1 is in", Cobra.current_room.room_name, "\n")
            print("Room description:", Cobra.current_room.description, "\n")
        else:
            print("Can not move there, no room to go to\n")
    
    if user_input == "e":
        if Cobra.current_room.e_to:
            Cobra.current_room = Cobra.current_room.e_to
            print("player moved east \n")
            print("Player 1 is in", Cobra.current_room.room_name, "\n")
            print("Room description:", Cobra.current_room.description, "\n")
        else:
            print("Can not move there, no room to go to\n")

    if user_input == "w":
        if Cobra.current_room.w_to:
            Cobra.current_room = Cobra.current_room.w_to
            print("player moved west! \n")
            print("Player 1 is in", Cobra.current_room.room_name, "\n")
            print("Room description:", Cobra.current_room.description, "\n")
        else:
            print("Can not move there, no room to go to\n")

    if user_input == "Cobra":
        add_room_item_input = input("Add item to room? y, n\n")
        if add_room_item_input == "y":
            new_item = input("Enter item name\n")
            Cobra.current_room.items.append(new_item)
            print(Cobra.current_room.room_name, "Items:", Cobra.current_room.items)
        elif add_room_item_input == "n":
            pass

        add_inventory_item = input("Add item to inventory? y, n\n")
        if add_inventory_item == 'y':
            new_inventory_item = input("Enter item name\n")
            Cobra.inventory.append(new_inventory_item)
            print(f"{Cobra.name}'s inventory: {Cobra.inventory}'")
