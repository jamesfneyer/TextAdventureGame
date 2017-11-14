from game import LockedDoors
from game import Inventory


class Rooms:

    def __init__(self, name, items, actions, locked):
        self.name = name
        self.items = items
        self.actions = actions
        self.locked = locked


    def create_room(self, name, items, actions, locked):
        self.name = name
        self.items = items
        self.actions = actions
        self.locked = locked

    def get_valid_item(self, room, item, desc, i):
        if item in room.items and item == desc:
            Inventory.inventory_items.append(item)
            print("You added the " + item + " to your inventory. Perhaps you can use it for something.")
        else:
            print("You are unable to add that to your inventory.")

    def get_valid_item_two_desc(self, room, item, desc1, desc2, i):
        if item in room.items and (item == desc1 or item == desc2):
            Inventory.inventory_items.append(item)
            print( "You added the " + item + " to your inventory. Perhaps you can use it for something.")
        else:
            print( "You are unable to add that to your inventory.")

    def main_room_action(room, action, item):
        for x in Inventory.inventory_items:
            print(x)
        if action == "inspect":
            return room.items[item]
        elif action == "get":
            if room.locked and item != "clothespin":
                print("You still cuffed. It's too far away to pick up.")
            else:
                Inventory.inventory_items.append(item)
                room.items.pop(item)
        elif action == "use":
            if room.name == "Main Room":
                if room.locked and item == "clothespin" and item in Inventory.inventory_items:
                    room.locked = False
                    Inventory.inventory_items.pop(item)
                    print("You use the clothespin to unlock your cuffs, breaking it in the process.")
                elif item == "hay":
                    room.items["clothespin"]="An ordinary clothespin. For some reason you think you can use it..."
                    room.items.pop(item)
                    print("Underneath the hay is an ordinary clothespin.")
                elif item == "bucket" and not room.locked:
                    room.items[
"key"]="It's the key to exit the room! Ooph, might not want to keep it longer than necessary."
                    room.items.pop(item)
                    print("At the bottom of the bucket underneath the... debris, is the key to the room!")
                elif item == "key" and item in inv:
                    i.pop(item)
                    print( "You unlock the door so you can leave the room.")
                else:
                    print( "That has no affect.")
            elif room.name == "A":
                if item == "broken down bed":
                    room.items["Two sturdy boards"]="Two sturdy boards. Perhaps you can use them to open a door..."
                    room.items.pop(item)
                    print( "Taking apart the bed, you found two sturdy boards.")
                else:
                    print( "That has no affect.")
            elif room.name == "B":
                if item == "shank":
                    Inventory.inventory_items.pop(item)
                    room.items["key to exit"]="It's the key to the exit! Now it's all covered in blood."
                    print( "You kill the cowering man, and he drops a key.")
                elif item == "man":
                    room.items["key to exit"]="It's the key to the exit!"
                    print( "You ask the man for the key. He gives it willingly, too scared to deny your request.")
                elif item == "mirror":
                    msg = "You take a long look at yourself in the mirror. Your face is gaunt, your eyes filled with a "
                    msg += "desire for blood. You know remember why you were in the cell alone, but did you deserve it?"
                    print( msg)
                else:
                    print( "That has no affect.")
            elif room.name == "C":
                if item == "sink":
                    room.items["key to east wing cell 2"]="It's the key to the next room!"
                    print( "You hear a metal clinking in the sink. There must be something down the drain.")
                else:
                    print( "That has no affect.")
            elif room.name == "D":
                if item == "toilet":
                    room.items["key to west wing cell 2"]="Inside the toilet, theres a key!"
                    msg = "You found a key inside the toilet! Odd, in a similar place as the first one"
                    print( msg+", and also to another cell.")
                else:
                    print( "That has no affect.")
            elif room.name == "F":
                if item == "pillow":
                    room.items["key to north wing cell 1"]="There's a key inside the pillowcase!"
                    print( "You found a key inside the pillowcase! Why do the prisoners have keys to all the cells?")
                else:
                    print( "That has no affect.")
            elif room.name == "E":
                if item == "poster":
                    room.items["axe"]="A crude axe hidden in a hole behind a pin-up poster."
                    msg = "Behind the poster is a shallowly dug hole. "
                    print( msg+"Inside is a crude axe. Why does it seem so familiar.")
                else:
                    print( "That has no affect.")
            elif room.name == "east wing":
                if item == "key to east wing cell 2" and item in inv:
                    Inventory.inventory_items.pop(item)
                    LockedDoors.locked_doors.pop("D")
                    LockedDoors.unlocked_doors.append("D")
                    print( "You unlock the door to east wing cell 2.")
                else:
                    print( "That has no affect.")
            elif room.name == "west wing":
                if item == "key to west wing cell 1" and item in inv:
                    Inventory.inventory_items.pop(item)
                    LockedDoors.locked_doors.pop("F")
                    LockedDoors.unlocked_doors.append("F")
                    print( "You unlock the door to west wing cell 1.")
                else:
                    print( "That has no affect.")
            elif room.name == "north wing":
                if item == "key to north wing cell 1" and item in inv:
                    i.remove_item(item)
                    LockedDoors.locked_doors.pop("A")
                    LockedDoors.unlocked_doors.append("A")
                    print( "You unlock the door to north wing cell 1.")
                elif item == "key to north wing cell 2" and item in inv:
                    i.remove_item(item)
                    LockedDoors.locked_doors.pop("B")
                    room.items["wooden bars"]="The doors to the cell are barred with wood."
                    LockedDoors.unlocked_doors.append("B")
                    print( "You unlock the door to north wing cell 2. But, you notice that the entrance is barred.")
                elif item == "axe" and item in inv:
                    i.remove_item(item)
                    LockedDoors.door_barred = False
                    msg = "You use the axe to savegly destroy the baricade to the cell door. "
                    print( msg+ "A somewhat familiar rage fills you as you do so.")
                else:
                    print( "That has no affect.")
            elif room.name == "south wing":
                if item == "key to exit" and item in inv:
                    i.remove_item(item)
                    LockedDoors.locked_doors.pop("Exit")
                    LockedDoors.unlocked_doors.append("Exit")
                    print( "You unlock the door to the exit.")
                else:
                    print( "That has no affect.")
            elif room.name == "exit":
                if item == "gun" and item in inv:
                    i.remove_item(item)
                    LockedDoors.game_over = True
                    msg = "You don't deserve to live with what you've done. You're a danger to everyone else around you"
                    msg += ". You decide to take matters in your own hands,"
                    print(  " and make sure you never harm another soul. The End.")
                elif item == "Door to leave":
                    msg = "You escape the prison. You don't know where you will go, or what exactly you will do. "
                    msg += "But you do know one thing, that someone, or some people, will pay for what happened.THE END"
                    LockedDoors.game_over = True
                    print( msg)
                else:
                    print( "That has no affect.")
        elif action == "get":
            if room.name == "Main Room":
                if item in room.items:
                    if room.locked:
                        if item == "clothespin" or item == "hay":
                            if item == "hay":
                                print( "You are unable to add that to your inventory.")
                            else:
                                Inventory.inventory_items.append(item)
                                print( "You added the" + item + "to your inventory. Perhaps you can use it.")
                        else:
                            print( "Those items are too far away to interact with.")
                    else:
                        return room.get_valid_item_two_desc(room, item, "shank", "key", i)
            elif room.name == "A":
                return room.get_valid_item(room, item, "Two Sturdy Boards", i)
            elif room.name == "B":
                return room.get_valid_item(room, item, "key to the exit", i)
            elif room.name == "C":
                return room.get_valid_item(room, item, "key to the east wing cell 2", i)
            elif room.name == "D":
                return room.get_valid_item(room, item, "key to the west wing cell 1", i)
            elif room.name == "F":
                return room.get_valid_item(room, item, "key to the west wing cell 2", i)
            elif room.name == "E":
                return room.get_valid_item(room, item, "axe", i)
            elif room.name == "Exit":
                return room.get_valid_item(room, item, "gun", i)