from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player_1 = Player('cobra g', room['outside'])


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
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w') \n")

    if user_input == 'n':
        if player_1.current_room.n_to:
            # change current room
            player_1.current_room = player_1.current_room.n_to
            print('player moved north \n')
            print('Player 1 is in', player_1.current_room.room_name, '\n')
            print('Room description:', player_1.current_room.description, '\n')
        else:
            print('Can not move there, no room to go to\n')

    if user_input == 's':
        if player_1.current_room.s_to:
            player_1.current_room = player_1.current_room.s_to
            print('player moved south \n')
            print('Player 1 is in', player_1.current_room.room_name, '\n')
            print('Room description:', player_1.current_room.description, '\n')
        else:
            print('Can not move there, no room to go to\n')
    
    if user_input == 'e':
        if player_1.current_room.e_to:
            player_1.current_room = player_1.current_room.e_to
            print('player moved east \n')
            print('Player 1 is in', player_1.current_room.room_name, '\n')
            print('Room description:', player_1.current_room.description, '\n')
        else:
            print('Can not move there, no room to go to\n')

    if user_input == 'w':
        if player_1.current_room.w_to:
            player_1.current_room = player_1.current_room.w_to
            print('player moved west! \n')
            print('Player 1 is in', player_1.current_room.room_name, '\n')
            print('Room description:', player_1.current_room.description, '\n')
        else:
            print('Can not move there, no room to go to\n')
