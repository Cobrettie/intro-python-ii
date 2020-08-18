from player import Player
from room import Room
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ['dirt', 'rock', 'shrub', 'insect']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['rustysword', 'emptychalice', 'shatteredarmor']),

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
player = Player('player', room['outside'])


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


print("A path you will go down, not knowing where it will lead you. Until we meet again, friend\n")

while True:
    user_input= input("Choose a direction to move in ('n', 's', 'e', 'w', or 'q' to quit)\n")

    if user_input == "q":
        break

    split_input = user_input.split()
    if len(split_input) == 1:
        direction_attribute = f"{user_input}_to"
        if hasattr(player.current_room, direction_attribute):
            player.current_room = getattr(player.current_room, direction_attribute)
            print(f"{player.current_room.room_name}. {player.current_room.description}\n")
            view_items = input("View this rooms items? y, n\n")
            if view_items == 'y':
                print(player.current_room.items)
            if view_items == 'n':
                print("On your way then...\n")

        else:
            print("Choose a valid direction or command \n")
            continue

    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == 'get':
            chosen_item = player.current_room.get_item(item_name)
            if chosen_item:
                # Item.on_take(chosen_item)
                player.current_room.remove_item(chosen_item)
                player.inventory.append(chosen_item)
                print(f"Grabbed item. You now have {player.inventory}\n")
            else:
                print(f"{item_name} does not exist in this room\n")





    if user_input == "Cobra":
        add_room_item_input = input("Add item to room? y, n\n")
        if add_room_item_input == "y":
            new_item = input("Enter item name\n")
            player.current_room.items.append(new_item)
            print(player.current_room.room_name, "Items:", player.current_room.items)
        elif add_room_item_input == "n":
            pass

        add_inventory_item = input("Add item to inventory? y, n\n")
        if add_inventory_item == 'y':
            new_inventory_item = input("Enter item name\n")
            player.inventory.append(new_inventory_item)
            print(f"{player.name}'s inventory: {player.inventory}'")







    # if user_input == "n":
    #     if player.current_room.n_to:
    #         # change current room
    #         player.current_room = player.current_room.n_to
    #         print(f"{player.name} moved north \n")
    #         print(f"{player.current_room.room_name}\n")
    #         print(f"{player.current_room.description}\n")
    #         view_items = input("View this rooms items? y, n\n")
    #         if view_items == 'y':
    #             print(player.current_room.items)
    #         if view_items == 'n':
    #             print("On your way then...\n")
    #     else:
    #         print("Can not move there, no room to go to\n")

    # if user_input == "s":
    #     if player.current_room.s_to:
    #         player.current_room = player.current_room.s_to
    #         print("player moved south \n")
    #         print("Player 1 is in", player.current_room.room_name, "\n")
    #         print("Room description:", player.current_room.description, "\n")
    #     else:
    #         print("Can not move there, no room to go to\n")
    
    # if user_input == "e":
    #     if player.current_room.e_to:
    #         player.current_room = player.current_room.e_to
    #         print("player moved east \n")
    #         print("Player 1 is in", player.current_room.room_name, "\n")
    #         print("Room description:", player.current_room.description, "\n")
    #     else:
    #         print("Can not move there, no room to go to\n")

    # if user_input == "w":
    #     if player.current_room.w_to:
    #         player.current_room = player.current_room.w_to
    #         print("player moved west! \n")
    #         print("Player 1 is in", player.current_room.room_name, "\n")
    #         print("Room description:", player.current_room.description, "\n")
    #     else:
    #         print("Can not move there, no room to go to\n")