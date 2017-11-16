from game import Inventory
from game import Rooms
from Rooms import Rooms
from game import LockedDoors


valid_locations = [
    "east wing cell 1","east wing cell 2","west wing cell 1","west wing cell 2",
    "exit","main room","north wing cell 1","north wing cell 2","north wing", "south wing", "east wing"]
main_room_items = {"shank": "A crude shank created out of nearby items. There's blood on it.",
                   "bucket": "Bucket used as a bathroom. Doesn't smell the best.",
                   "door": "The door to the room. It looks locked",
                   "hay": "A pile of hay. Looks like there's something underneath?"}
actions = ["inspect", "get", "use","see inventory","look at surroundings","move"]
north_wing_exits = ["main room", "west wing", "east wing", "north wing cell 1", "north wing cell 2"]
room_A_items = {
    "broken down bed":"This bed has been broken heavily down. The frame still looks sturdy however.",
    "bloodied man":"A man lies down on the ground. His throat has been slit with a shank.",
    "broken mirror": "The mirror over the sink is broken. What happened?",
    "door": "The door to the hallway is wide-open."
    }
room_B_items = {
    "bed" : "A bed lies in the corner, well-used.",
    "mirror" : "A functioning mirror",
    "man":"A man cowering in the corner. He seems familiar...",
    "door": "The door to the hallway is wide-open."
}
room_C_items = {
    "bed" : "A bed lies in the corner. It is rotten, with no possible use remaining.",
    "mirror" : "A shattered mirror lays hanging in the corner.",
    "man":"A man is shoved with his head down the toilet, obviously dead. For some reason, you know he deserved it.",
    "sink":"A sink stands in the corner. It still seems to be functional.",
    "boor": "The door to the hallway is wide-open."
}
room_D_items = {
    "bed" : "A bed lies in the corner. It is rotten, with no possible use remaining.",
    "mirror" : "A functioning mirror",
    "toilet": "A used toilet. Foul smells emanate from it.",
    "man":"A man hangs from the ceiling. He must have killed himself. Too convenient of a death for him.",
    "door": "The door to the hallway is wide-open."
}
room_E_items = {
    "Bed" : "A bed lies in the corner. For some reason you know just how comfortable it is.",
    "mirror" : "A functioning mirror",
    "toilet": "A used toilet. Foul smells emanate from it.",
    "man":"A man hangs from the ceiling. He must have killed himself. Too convenient of a death for him.",
    "poster": "A pin-up poster hangs on the wall.",
    "Door": "The door to the hallway is wide-open."
}
room_F_items = {
    "bed" : "A bed lies in the corner. A man lies on it, his life choked out of him by a pillow.",
    "pillow":"A pillow lies on top of the dead man, ensuring he made no sound as he died.",
    "mirror" : "A functioning mirror",
    "toilet": "A used toilet. Foul smells emanate from it.",
    "man":"A man hangs from the ceiling. He must have killed himself. Too convenient of a death for him.",
    "door": "The door to the hallway is wide-open."
}
room_Exit_items = {
    "door to hallway" : "The door to go back to the hallway.",
    "door to leave" : "The door to exit the jail.",
    "gun" : "A gun lies in the room, with some ammo next to it."
}
north_wing_items = {
    "door to north wing cell 1" : "The door to cell 1 of the north wing.",
    "door to north wing cell 2" : "The door to cell 2 of the north wing.",
    "west wing": "The west wing of the cell block.",
    "east wing": "The east wing of the cell block."
}
west_wing_items = {
    "door to west wing cell 1" : "The door to cell 1 of the west wing.",
    "door to west wing cell 2" : "The door to cell 2 of the west wing.",
    "north wing": "The north wing of the cell block.",
    "south wing": "The south wing of the cell block."
}
east_wing_items = {
    "door to east wing cell 1" : "The door to cell 1 of the east wing.",
    "door to east wing cell 2" : "The door to cell 2 of the east wing.",
    "north wing": "The north wing of the cell block.",
    "south wing": "The south wing of the cell block."
}
south_wing_items = {
    "door to exit":"The door to the exit of the jail.",
    "west wing": "The west wing of the cell block.",
    "east wing": "The east wing of the cell block."
}
location = "main room"
door_barred = True
game_over = False
main_room = Rooms(name = "Main Room", items = main_room_items, actions = actions, locked = True)
room_A = Rooms(name = "A", items = room_A_items, actions = actions, locked = True)
room_B = Rooms(name = "B", items = room_B_items, actions = actions, locked = True)
room_C = Rooms(name = "C", items = room_C_items, actions = actions, locked = False)
room_D = Rooms(name = "D", items = room_D_items, actions = actions, locked = True)
room_E = Rooms(name = "E", items = room_E_items, actions = actions, locked = False)
room_F = Rooms(name = "F", items = room_F_items, actions = actions, locked = True)
room_Exit = Rooms(name = "D", items = room_Exit_items, actions = actions, locked = True)
north_wing = Rooms(name = "north wing", items = north_wing_items, actions = actions, locked = False)
east_wing = Rooms(name = "east wing", items = east_wing_items, actions = actions, locked = False)
west_wing = Rooms(name = "west wing", items = east_wing_items, actions = actions, locked = False)
south_wing = Rooms(name = "south wing", items = east_wing_items, actions = actions, locked = False)


def get_location():
    global location
    if location == "north wing cell 1":
        return room_A
    elif location == "north wing cell 2":
        return room_B
    elif location == "east wing cell 1":
        return room_C
    elif location == "east wing cell 2":
        return room_D
    elif location == "west wing cell 2":
        return room_E
    elif location == "west wing cell 1":
        return room_F
    elif location == "main room":
        return main_room
    elif location == "north wing":
        return north_wing
    elif location == "south wing":
        return south_wing
    elif location == "west wing":
        return west_wing
    elif location == "east wing":
        return east_wing
    elif location == "exit":
        return room_Exit


def get_valid_item():
    isvalid = False
    location_items = get_location_items()
    while not isvalid:
        command = input("What item would you like to use? ")
        if command.lower() == "back":
            return "back"
        elif command.lower() not in location_items and command.lower() not in Inventory.inventory_items:
            print("That is not something you can use. Enter back to go back.")
        else:
            isvalid = True
            return command.lower()


def get_valid_command():
    isvalid = False
    while not isvalid:
        command = input("What would you like to do? (Inspect/Get/Use/See Inventory/Look at surroundings) ")
        if command.lower() not in actions:
            print("That's not a valid command!")
        else:
            isvalid = True
            return command.lower()


def get_location_items():
    location =  LockedDoors.location
    if location == "north wing cell 1":
        return room_A_items
    elif location == "north wing cell 2":
        return room_B_items
    elif location == "east wing cell 1":
        return room_C_items
    elif location == "east wing cell 2":
        return room_D_items
    elif location == "west wing cell 2":
        return room_E_items
    elif location == "west wing cell 1":
        return room_F_items
    elif location == "main room":
        return main_room_items
    elif location == "north wing":
        return north_wing_items
    elif location == "south wing":
        return south_wing_items
    elif location == "west wing":
        return west_wing_items
    elif location == "east wing":
        return east_wing_items
    elif location == "exit":
        return room_Exit_items


def inspect_item():
    isvalid = False
    items = get_location_items()
    while not isvalid:
        choice = input("What would you like to inspect? ")
        if choice.lower() in items:
            isvalid = True
            print(items[choice.lower()])
        elif choice.lower() == "back":
            isvalid = True
        else:
            print("Invalid item to inspect. Enter back to go back.")


def look_at_surroundings():
    for x in get_location_items():
        print(x)


"""def get_valid_move():
    global location
    isvalid = False
    while not isvalid:
        command = input("What room would you like to move to? ")
        if command.lower() in valid_locations:
            if command.lower == "north wing":
                if location not in north_wing_exits:
                    print("Error! Cannot move to that location from here.")
                elif location == "main room" and "Main Room" in LockedDoors.unlocked_doors:
                    location = "north wing"
                    isvalid = True
                    print("You move to the north wing.")
                elif location == "main room" and "Main Room" in LockedDoors.locked_doors:
                    print("The door is locked. You cannot enter.")
                else:
                    location = "north wing"
                    isvalid = True
                    print("You move to the north wing.")
            elif command.lower == "west wing":
                if location != ("north wing" or "south wing" or "west wing cell 1" or "west wing cell 2"):
                    print("Error! Cannot move here from that location.")
                else:
                    location = "west wing"
                    isvalid = True
                    print("You move to the west wing.")
            elif command.lower == "east wing":
                if location != ("north wing" or "south wing" or "east wing cell 1" or "east wing cell 2"):
                    print("Error! Cannot move here from that location.")
                else:
                    location = "east wing"
                    isvalid = True
                    print("You move to the east wing.")
            elif command.lower == "south wing":
                if location != ("north wing" or "south wing" or "exit"):
                    print("Error! Cannot move here from that location.")
                else:
                    location = "east wing"
                    isvalid = True
                    print("You move to the east wing.")
            elif command.lower == "east wing cell 1":
                if location == ("east wing"):
                    location = "east wing cell 1"
                    isvalid = True
                    print("You move to the east wing cell 1.")
                else:
                    print("You cannot move to this room for your location.")
            elif command.lower == "east wing cell 2":
                if location != ("east wing"):
                    print("You cannot move to this room for your location.")
                elif "D" in LockedDoors.locked_doors:
                    print("The door is locked. You cannot enter yet.")
                elif "D" in LockedDoors.unlocked_doors:
                    location = "east wing cell 2"
                    isvalid = True
                    print("You move to the east wing cell 2.")
            elif command.lower == "west wing cell 2":
                if location == ("west wing"):
                    location = "west wing cell 2"
                    isvalid = True
                    print("You move to the west wing cell 2.")
                else:
                    print("You cannot move to this room for your location.")
            elif command.lower == "west wing cell 1":
                if location != ("west wing"):
                    print("You cannot move to this room for your location.")
                elif "F" in LockedDoors.locked_doors:
                    print("The door is locked. You cannot enter yet.")
                elif "F" in LockedDoors.unlocked_doors:
                    location = "west wing cell 1"
                    isvalid = True
                    print("You move to the east wing cell 2.")
            elif command.lower == "north wing cell 1":
                if location != ("north wing"):
                    print("You cannot move to this room for your location.")
                elif "A" in LockedDoors.locked_doors:
                    print("The door is locked. You cannot enter yet.")
                elif "A" in LockedDoors.unlocked_doors:
                    location = "north wing cell 1"
                    isvalid = True
                    print("You move to the north wing cell 1.")
            elif command.lower == "north wing cell 2":
                if location != ("north wing"):
                    print("You cannot move to this room for your location.")
                elif "B" in LockedDoors.locked_doors:
                    print("The door is locked. You cannot enter yet.")
                elif door_barred:
                    print("The doorway is blocked by wood. You cannot enter yet.")
                elif "B" in LockedDoors.unlocked_doors and not door_barred:
                    location = "north wing cell 2"
                    isvalid = True
                    print("You move to the north wing cell 2.")
        elif command.lower() == "back":
            return "back"
        else:
            print("Invalid location to move to. Enter back to go back.")"""


def get_valid_object():
    isvalid = False
    area_items = get_location_items()
    while not isvalid:
        command = input("What would you like to get? ")
        if command.lower() not in get_location_items():
            print("That is not an object in your immediate area. Type back to go back.")
        elif command.lower() == "back":
            isvalid = True
            return command.lower()
        else:
            isvalid = True
            return command.lower()


print("You wake up in a cell, handcuffed to the wall.")
while not game_over:
    choice = get_valid_command()
    if choice == "see inventory":
        items = Inventory.inventory_items
        for x in items:
            print(x)
    elif choice == "look at surroundings":
        look_at_surroundings()
    elif choice == "inspect":
        inspect_item()
    elif choice == "use":
        item = get_valid_item()
        room = get_location()
        if item != "back":
            Rooms.main_room_action(room = room, action = choice, item = item)
    elif choice == "get":
        item = get_valid_object()
        room = get_location()
        if item != "back":
            Rooms.main_room_action(room = room, action = choice, item = item)
    elif choice == "move":
        move = get_valid_move()

