import time
from Objects.Character import Character  # Import Character class for player object handling
from Functions.intro import sequence
import os

def openItem(current_location, playerInventory, noun, player, events) :

    locationId = current_location['id'] # Get the current location ID

    if noun == 'book' and locationId == 'church library':
        # If the player tries to open a book in the church library
        sequence('book', events) # Display text associated with the book
        input("\n\nPress enter when done\n") # Pause for user to read the text
    
    elif locationId == 'church library' and current_location['puzzle']['opened']:
        # If the puzzle in the church library is already opened
        print("The chest is empty.") # Inform the player that the chest is empt
        time.sleep(2) # Brief pause for readability

    elif locationId == 'church library' and not current_location['puzzle']['opened']:
    # If there's an unopened puzzle in the church library
        answer = ''
        while answer != 'l':

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"The chest is locked, but this is a riddle inscribed above. It reads:", current_location['puzzle']['riddle'])
            answer = input("\nWhat will you enter into the combination lock? Enter 'L' to leave.\n").lower()  # Prompt for puzzle solution

            if answer in current_location['puzzle']['solution']:
                print("\nIt worked! You found a key!") # Success message
                player.pick_up_item('basement key', current_location) # Add basement key to player's inventory
                current_location['puzzle']['opened'] = True # Mark the puzzle as opened
                break

            elif answer == 'l':
                break
            else:
                input("Hmm, that didn't work..\n\nPress enter to try again.")

    
    elif locationId == 'church entrance':
        # If the player is trying to open something at the church entrance
        if 'basement key' in playerInventory:
            # If the player has the basement key
            print("\nThe latch opens! Stairs lead into the basement cellar to the north.. You hear something moving in the darkness")
            input("Press enter to continue...")


