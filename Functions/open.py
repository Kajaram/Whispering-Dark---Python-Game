import time
from Objects.Character import Character
from Functions.inventoryFunctions import pick_up_item

def openItem(current_location, playerInventory, noun) :

    locationId = current_location['id']

    if noun == 'book' and locationId == 'church_library':
        print(current_location['text'])
        input("\n\nPress enter when done")
    
    elif locationId == 'church_library' and current_location['puzzle']['opened']:
        print("The chest is empty.")
        time.sleep(2)

    elif locationId == 'church_library' and not current_location['puzzle']['opened']:

        print(f"The chest is locked, but this is a riddle inscribed above. It reads:", current_location['puzzle']['riddle'])
        current_location['puzzle']['opened'] = True
        answer = input("\nWhat will you enter into the combination lock? Enter 'L' to leave.\n")

        if answer in current_location['puzzle']['solution']:
            print("\nIt worked! You found a key!")
            pick_up_item('basement_key', playerInventory, current_location)
    
    elif locationId == 'church_entrance':

        if 'basement_key' in playerInventory:
            print("\nThe latch opens! Stairs lead into the basement cellar to the north.. You hear something moving in the darkness")
            time.sleep(3)


