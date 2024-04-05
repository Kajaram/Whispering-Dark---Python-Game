from Functions.locationFunctions import get_location
from Objects.Character import Character
from Functions.intro import sequence
import time
import os

def use_item(item_name, current_location, player_inventory, player,events=''):
    if item_name in player_inventory:
            # Trigger event outcome here
        if item_name == 'flashlight' and current_location['id'] == 'church_entrance':
            print("The flashlight illuminates the inside of the church.\nExpansive murals line its walls, their glistening colours telling tales of both glory and woe.")
            input("Press enter to continue...")
            # Modify location exits or reveal items
        elif item_name == 'walkie' and current_location['id'] == 'radio_tower':
            sequence('radio_tower', events)
            print("\n\nCongratulations! help is on its way.\nYou survived the clutches of the evil cultists and the wendigo.\nFeel free to explore or type 'quit' to exit.")
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