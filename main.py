from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.inventoryFunctions import pick_up_item, use_item
from Functions.engine import load_game_data
from Functions.intro import introSequence
from Functions.quickTime import timer
import os
import time

locations = load_game_data('assets/Whispering-Dark Updated.json')  # Adjust the path as necessary
current_location = get_location('cabin', locations)  # Starting location
inventory = []
health = 100

# Main game loop
if __name__ == '__main__':
    
    # menu()
    introSequence()

    locations = load_game_data('assets/Whispering-Dark Updated.json')  # Adjust the path as necessary
    current_location = get_location('cabin', locations)  # Starting location
    
    print("\nWelcome to Whispering Dark. Type 'quit' to exit at any time.")
    describe_location(current_location)

    while True:

        os.system('cls')
        command = input("\nWhat do you want to do?\n").strip().lower()
        command = command.split()
        
        
        if len(command) > 0:
            if command[0] == 'quit':
                print("Thanks for playing. Goodbye!")
                time.sleep(4)
                os.system('cls')
                break

            elif command[0] in ['move', 'go', 'walk', 'travel','run']:
                current_location, moved = move_player(command[1], current_location, locations, inventory)
                
                if not moved:
                    print("You can't move in that direction..")
                    time.sleep(2)
                else:

                    describe_location(current_location)

                    if current_location['id'] == 'trail':
                        timer(7)
                        
                    else:    
                        continue

            # elif command in ['pick up', 'grab', 'equip'] :
            #     pick_up_item()
            else:
                print("Unknown command. Please try again.")

        else:
            print("Please enter a command..")
