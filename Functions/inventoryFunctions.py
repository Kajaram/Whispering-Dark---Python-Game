from Functions.locationFunctions import get_location
from Objects.Character import Character
from Functions.intro import sequence
import time
import os


def drop_item(item_name, current_location, player):
    current_location['items'].append(item_name)
    player.removeFromInventory(item_name)
    print(f"Item Dropped")
    input("\nPress enter...")


def use_item(item_name, current_location, player_inventory, player,events=''):
    if item_name in player_inventory:
            # Trigger event outcome here
        if item_name == 'flashlight' and current_location['id'] == 'church entrance':
            print("The flashlight illuminates the inside of the church.\nExpansive murals line its walls, their glistening colours telling tales of both glory and woe.")
            input("Press enter to continue...")
            # Modify location exits or reveal items
        elif item_name == 'walkie' and current_location['id'] == 'radio tower':
            sequence('radio_tower', events)

        elif item_name == 'bandages':
            player.setHealth(15)
            print(f"{player.getCustomName()} used a bandage! \nYour health increases by 15 points")
            print(f"Player health: ", player.getHealth())
            player.removeFromInventory('bandages')
            input("\nPress enter to continue...")

        elif item_name == 'map':
            exits = current_location['exits']
            for key, val in exits.items():
                print(f"\n{key} --> {val}")
    
            input("\nPress enter to continue...")
        
        else:
            print(f"\nYou use the {item_name}, but nothing happens.")
            input("\nPress enter to continue...")
    else:
        print("\nYou don't have that item.")
        input("\nPress enter to continue...")

# Example of picking up an item
def pick_up_item(item_name, player_inventory, current_location,player):
    
    current_location_items = current_location['items']
    if item_name in current_location_items:
        player_inventory.append(item_name)
        current_location_items.remove(item_name)
        print(f"Picked up {item_name}.")

        if item_name == 'talisman':
            os.system('cls')
            print("The talisman grants you additional health.\nYou will now have twice as many health points as you currently have.")
            player.setHealth(2*player.getHealth())
            print(f"Player health: {player.getHealth()}")
        input("\nPress enter to continue...")
    
    elif item_name in player_inventory:
        print(item_name + " is already in your inventory.")
        input("\nPress enter to continue...")

    else:
        print("That item isn't here.")
        input("\nPress enter to continue...")