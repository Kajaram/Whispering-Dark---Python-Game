from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.inventoryFunctions import pick_up_item, use_item, drop_item
from Functions.engine import load_game_data,check_event_happened, set_event_happened
from Functions.intro import sequence
from Functions.quickTime import timer
from Objects.Character import Character
from Functions.fight import fightFunc
from Functions.open import openItem
from Functions.save_system import save_game, load_game
from Functions.mainMenu import mainMenu
import os
import time

# Change current working directory to the directory where the script is located
os.chdir(os.path.dirname(__file__))

# import sys
# sys.path.append('c:\python312\lib\site-packages')

locations = load_game_data('Whispering-Dark Updated.json', 'locations')  # Load location data 
events = load_game_data('Whispering-Dark Updated.json', 'events') # Load event data
dialogue = load_game_data('Whispering-Dark Updated.json', 'dialogue') # Load dialogue data
items = load_game_data('Whispering-Dark Updated.json', 'items')  # Load item data
current_location = get_location('cabin', locations) # Get initial location

player = Character(100, 'player') # Initialize player character
wendigo = Character(200, 'wendigo', 40) # Initialize wendigo character
cultist = Character(30, 'cultist', 30) # Initialize cultist character

# Initialize NPC
evelyn = Character(50)
sophia = Character(100)
rohan = Character(100)
ava = Character(100)
daniel = Character(100)


# Main game loop
if __name__ == '__main__':

    cultist.setCustomName('cultist') 
    wendigo.setCustomName('wendigo') 

    
    loaded = mainMenu(player, locations, wendigo, cultist, events, current_location)

    #Check if player has loaded from a save state. If not, start new game

    if not loaded:
        myName = input('\nEnter your Name:\n\n')
        print("\nWelcome,", myName)
        input("\nPress enter...\n")
        player.setCustomName(myName) # Set player name
        os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
        sequence('intro_cutscene', events, player, cultist, dialogue, items) # Play intro cutscene
        sequence('cabin', events, player, cultist, dialogue, items)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nWelcome to Whispering Dark. \nType 'quit' to exit at any time and 'pause' for the menu.")
        input("\n\nPress enter to continue...")

    else: # Load game state if loaded from save
        loaded_state = load_game()
        player.from_dict(loaded_state["player"])
        wendigo.from_dict(loaded_state["wendigo"])
        cultist.from_dict(loaded_state["cultist"])
        events = loaded_state["events"]
        locations=loaded_state['locations']
        current_location = get_location(loaded_state["current_location_id"], locations)
        
    os.system('cls' if os.name == 'nt' else 'clear')
    started = True

    while True:
       
        os.system('cls' if os.name == 'nt' else 'clear') # Clear screen

        describe_location(current_location) # Describe the current location

        command = input("\nWhat do you want to do?\n").strip().lower()
        command = command.split()
        
        
        if len(command) > 0:
            if command[0] == 'quit': # Quit game command
                print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                time.sleep(3)
                # os.system('cls')
                break

            #Read commands for movement, pause, item use, etc.

            elif command[0] in ['pause', 'menu','start','options']: # Open game menu
                 mainMenu(player, locations, wendigo, cultist, events, current_location, loaded, started)

            
            elif command[0] == 'inventory': # Show player inventory
                player.showInventory()
                input("\nPress enter to continue...")


            elif command[0] in ['move', 'go', 'walk', 'travel','run', 'n', 'e', 'w', 's']: # Move player to a new location
                
                

                if command[0] in ['n', 'e', 'w', 's']: # Move player to a new location

                    newcommand = command[0]

                    if command[0] == 'n':
                        newcommand = 'north'

                    elif command[0] == 'e':
                        newcommand = 'east'
                    
                    elif command[0] == 's':
                        newcommand = 'south'
                    
                    elif command[0] == 'w':
                        newcommand = 'west'
                else:
                    newcommand = command[1]
                  
                current_location, moved = move_player(newcommand, current_location, locations, player.getInventory())

                if not moved:
                    input("\nPress enter to continue...")

                #Check current location to initiate text and fight sequences

                else:

                    if current_location['id'] == 'trail' and not wendigo.checkIsDead() and 'axe' in player.getInventory():
                         sequence('wendigo_confrontation', events, player, wendigo, dialogue, items)
                      

                    elif current_location['id'] == 'church entrance':
                         sequence('church_discovery', events, player, cultist, dialogue, items)   


                    elif current_location['id'] == 'church basement' and not cultist.checkIsDead():
                        sequence('basement_confrontation', events, player, cultist, dialogue, items)
                        

                    elif current_location['id'] == 'radio tower':
                        os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
                        describe_location(current_location)
                        input("Press enter to continue...")
                        sequence('radio_tower2', events)
                        

                    else:    
                        continue

                if player.checkIsDead() : # Check if player is dead
                        print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                        break
        

            elif command[0] in ['grab', 'take', 'equip'] :  # Player picks up an item
                pick_up_item(command[1], player.getInventory(), current_location, player)

            elif command[0] in ['drop'] :  # Player picks up an item
                drop_item(command[1], current_location, player)

            elif command[0] in ['open', 'unlock', 'read']:  # Player opens or reads an item
                openItem(current_location, player.getInventory(), command[1], player, events)

            elif command[0] in ['use']:  # Player uses an item
                use_item(command[1], current_location ,player.getInventory(), player, events)

            else:
                print("\nUnknown command. Please try again.")
                time.sleep(2)


        else:
            print("\nPlease enter a command..")
            time.sleep(2)
