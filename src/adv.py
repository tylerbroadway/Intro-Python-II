from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("old map", "old, washed up map")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("pocket watch", "holds a picture of some man.")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("parasail", "for jumping from the overlook.")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("flashlight", "does it even work?")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("golden sword", "old, but still shiny.")),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

starting_room = room["outside"]
player = Player("Tyler", starting_room)

while True:
  current_room = player.current_room
  player_inventory = [x for x in player.inventory] if len(player.inventory) else   "No Inventory"
  room_inventory = [x for x in current_room.items] if len(current_room.items) else "Empty Room"

  verb, obj = "", ""
  
  print(f"Current Room: {current_room}\n")
  print(f"Inventory: {player.inventory}\n")
  print(f"Which direction would you like to move?\n")

  cmd = input("Press 'n', 'e', 's', or 'w' to move. Press 'q' to quit. You can also pick up or drop items, by saying 'Take item' or 'Drop item'.\n")

  if "take" in cmd:
    verb = cmd.split(" ")
    if len(verb) == 2:
      obj = verb[1]
      for item in current_room.items:
        if item.name == obj:
          player.take_item(item)
          # current_room.remove_item(item.name)
    if len(verb) == 3:
      obj = verb[1] + ' ' + verb[2]
      for item in current_room.items:
        if item.name == obj:
          player.take_item(item)
          # current_room.remove_item(item.name)
        else:
          continue
  
  if "drop" in cmd:
    verb = cmd.split(" ")
    if len(verb) == 2:
      obj = verb[1]
      for item in current_room.items:
        if item.name == obj:
          player.drop_item(item)
          # current_room.add_item(item.name)
    if len(verb) == 3:
      obj = verb[1] + ' ' + verb[2]
      for item in current_room.items:
        if item.name == obj:
          player.drop_item(item)
          # current_room.add_item(item.name)
        else:
          continue

  if cmd == 'q':
    print("\nThank you for playing.\n")
    break
  elif cmd == 'n':
    if hasattr(current_room, "n_to"):
      print("\nHeading north...\n")
      player.current_room = current_room.n_to
    else:
      print("\nCannot head north. Try another direction.\n")
  elif cmd == 'e':
    if hasattr(current_room, "e_to"):
      print("\nHeading east...\n")
      player.current_room = current_room.e_to
    else:
      print("\nCannot head east. Try another direction.\n")
  elif cmd == 's':
    if hasattr(current_room, "s_to"):
      print("\nHeading south...\n")
      player.current_room = current_room.s_to
    else:
      print("\nCannot head south. Try another direction.\n")
  elif cmd == 'w':
    if hasattr(current_room, "w_to"):
      print("\nHeading west...\n")
      player.current_room = current_room.w_to
    else:
      print("\nCannot head west. Try another direction.\n")
  else:
    # print("\nInvalid command. Use 'n', 'e', 's', and 'w' to move, or press 'q' to quit.\n")
    pass
