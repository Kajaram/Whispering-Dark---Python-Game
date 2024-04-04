from Functions.locationFunctions import get_location
import time

def use_item(item_name, current_location, player_inventory):
    if item_name in player_inventory:
        if item_name == 'silver_axe' and current_location['id'] == 'wendigo_lair':
            print("You use the silver axe to defeat the Wendigo!")
            # Trigger event outcome here
        elif item_name == 'flashlight' and current_location['id'] == 'dark_forest':
            print("The flashlight reveals a hidden path!")
            # Modify location exits or reveal items
        else:
            print(f"You use the {item_name}, but nothing happens.")
    else:
        print("You don't have that item.")

# Example of picking up an item
def pick_up_item(item_name, player_inventory, current_location):
    
    current_location_items = current_location['items']
    if item_name in current_location_items:
        player_inventory.append(item_name)
        current_location_items.remove(item_name)
        print(f"Picked up {item_name}.")
        time.sleep(3)
    
    elif item_name in player_inventory:
        print(item_name + "is already in your inventory.")
        time.sleep(2)

    else:
        print("That item isn't here.")
        time.sleep(3)