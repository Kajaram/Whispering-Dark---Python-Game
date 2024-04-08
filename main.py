from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.engine import load_world,check_event_happened, set_event_happened, load_world
from Functions.intro import sequence
from Functions.quickTime import timer
from Objects.Character import Character
from Functions.fight import fightFunc
from Functions.open import openItem
from Functions.save_system import save_game, load_game
from Functions.mainMenu import mainMenu
from Factories.characterFactory import characterFactory
import os
import time

# Change current working directory to the directory where the script is located
os.chdir(os.path.dirname(__file__))


world = load_world('Whispering-Dark Updated.json', 'world')  # Load world data from JSON 
# print(world)
locations = world['locations'] # Load location data 
events = world['events'] # Load event data
dialogue = world['dialogue'] # Load dialogue data
items = world['items'] # Load item data

current_location = get_location('cabin', locations) # Get initial location

factory = characterFactory()

cultist = factory.makeCharacter('cultist')
wendigo = factory.makeCharacter('wendigo')


flag = False
started = False
loaded = False

# Main game loop
if __name__ == '__main__':

    while True:

        if flag: break
        newWorld, loaded1 = mainMenu(world, loaded, started)
        started = True
        #Check if player has loaded from a save state. If not, start new game

        if not loaded1:
            myName = input('\nEnter your Name:\n\n').strip()
            print("\nWelcome,", myName)
            input("\nPress enter...\n")
            player = factory.makeCharacter('player', myName) # Set player name
            
            os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
            sequence('intro_cutscene', events, player, cultist, dialogue, items) # Play intro cutscene
            sequence('cabin', events, player, cultist, dialogue, items)

            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("\nWelcome to Whispering Dark. \nType 'quit' to exit at any time and 'pause' for the menu.")
            input("\n\nPress enter to continue...")


        else: # Load game state if loaded from save
            world = newWorld
            locations = world['locations'] # Load location data 
            events = world['events'] # Load event data
            dialogue = world['dialogue'] # Load dialogue data
            items = world['items'] # Load item data
            current_location = get_location(world['current_location'], locations) # Get initial location
                
        loaded = True
        os.system('cls' if os.name == 'nt' else 'clear')
        started = True
        player.addToInventory("")

        while True:
            
          
            os.system('cls' if os.name == 'nt' else 'clear') # Clear screen

            describe_location(current_location) # Describe the current location

            command = input("\nWhat do you want to do?\n").strip().lower()
            command = command.split()
            
            
            if len(command) > 0:

                if command[0] == 'quit': # Quit game command
                    print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                    time.sleep(2)
                    flag = True
                    break

                #Read commands for movement, pause, item use, etc.

                elif command[0] in ['pause', 'menu','start','options']: # Open game menu
                    newWorld, loaded2 = mainMenu(world,loaded)

                    if loaded2:
                                world = newWorld
                                locations = world['locations'] # Load location data 
                                events = world['events'] # Load event data
                                dialogue = world['dialogue'] # Load dialogue data
                                items = world['items'] # Load item data
                                current_location = get_location(world['current_location'], locations) # Get initial location

                
                elif command[0] == 'inventory': # Show player inventory
                    player.showInventory()
                    input("\nPress enter to continue...")


                elif command[0] in ['move', 'go', 'walk', 'travel','run', 'n', 'e', 'w', 's']: # Move player to a new location
                    

                    if command[0] in ['n', 'e', 'w', 's']: # filter input for json requests

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

                    if moved:
                       
                    #Check current location to initiate text and fight sequences

                        if current_location['id'] == 'trail':
                            sequence('wendigo_confrontation', events, player, wendigo, dialogue, items)
                        

                        elif current_location['id'] == 'church entrance':
                            sequence('church_discovery', events, player, cultist, dialogue, items)   


                        elif current_location['id'] == 'church basement':
                            sequence('basement_confrontation', events, player, cultist, dialogue, items)
                            

                        elif current_location['id'] == 'radio tower':
                            os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
                            describe_location(current_location)
                            input("Press enter to continue...")
                            sequence('radio_tower2', events)
                            

                        else:    
                            continue

                    else:
                        continue

                    if player.checkIsDead() : # Check if player is dead
                            print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                   
                            break
                
                    

            
                elif len(command) > 1:

                    if command[0] in ['grab', 'take', 'equip'] :  # Player picks up an item
        
                        player.pick_up_item(command[1], current_location)

                    elif command[0] in ['drop'] :  # Player picks up an item
                        if len(command) >= 2:
                            player.drop_item(command[1], current_location)

                        else:
                            input("\nIncorrect # of arguments.\n\nPress enter...")

                    elif command[0] in ['open', 'unlock', 'read']:  # Player opens or reads an item

                        openItem(current_location, player.getInventory(), command[1],player, events)

                    elif command[0] in ['use']:  # Player uses an item
                        player.use_item(command[1], current_location , events)

                else:
                    print("\nUnknown command. Please try again.")
                    time.sleep(2)


            else:
                print("\nUnknown command..")
                time.sleep(2)
