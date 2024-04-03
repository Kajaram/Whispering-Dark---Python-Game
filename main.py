from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.inventoryFunctions import pick_up_item, use_item
from Functions.engine import load_game_data
from Functions.intro import introSequence
from Functions.quickTime import timer
from Objects.Character import Character
from Functions.fight import fightFunc
import os
import time
import sys

player = Character("Player", 100)
wendigo = Character("Wendigo", 200)
cultist = Character("Cultist", 50)

sys.path.append('c:\python312\lib\site-packages')

locations = load_game_data('assets/Whispering-Dark Updated.json')  # Adjust the path as necessary
current_location = get_location('cabin', locations)  # Starting location


# Main game loop
if __name__ == '__main__':
    
    # menu()
    introSequence()

    locations = load_game_data('assets/Whispering-Dark Updated.json')  # Adjust the path as necessary
    current_location = get_location('cabin', locations)  # Starting location
    
    print("\nWelcome to Whispering Dark. Type 'quit' to exit at any time.")

    while True:

        os.system('cls')
        describe_location(current_location)
        command = input("\nWhat do you want to do?\n").strip().lower()
        command = command.split()
        
        
        if len(command) > 0:
            if command[0] == 'quit':
                print("Thanks for playing. Goodbye!")
                time.sleep(3)
                os.system('cls')
                break

            elif command[0] in ['move', 'go', 'walk', 'travel','run']:
                current_location, moved = move_player(command[1], current_location, locations, player.getInventory())
                
                if not moved:
                    print("You can't move in that direction..")
                    time.sleep(2)
                else:

                    os.system('cls')
                    describe_location(current_location)

                    if current_location['id'] == 'trail':
                        fightFunc(player, wendigo, current_location, locations)
                        
                        
                    else:    
                        continue

            # elif command in ['pick up', 'grab', 'equip'] :
            #     pick_up_item()
            else:
                print("Unknown command. Please try again.")

        else:
            print("Please enter a command..")
