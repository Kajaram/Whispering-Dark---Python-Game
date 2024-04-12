from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.engine import load_world, load_world
from Functions.sequences import sequence
from Objects.Character import Character
from Functions.open import openItem
from Functions.mainMenu import mainMenu
from Factories.characterFactory import characterFactory
from Functions.newSave import load_game_state
import os
import time

# Change current working directory to the directory where the script is located
os.chdir(os.path.dirname(__file__))

comDict = {"n" : "north", "e":"east", "w":"west", "s":"south"}
world = load_world('Whispering-Dark Updated.json', 'world')  # Load world data from JSON 
locations = world['locations'] # Load location data 
events = world['events'] # Load event data
dialogue = world['dialogue'] # Load dialogue data
items = world['items'] # Load item data
current_location = get_location('cabin', locations) # Get initial location

factory = characterFactory()

cultist = factory.makeCharacter('cultist')
wendigo = factory.makeCharacter('wendigo')
player = factory.makeCharacter('player')


flag = False
started = False
loaded = False

# Main game loop
if __name__ == '__main__':

    while True:
        
        if flag: break
        loaded1, freshStart = mainMenu(wendigo, cultist, world, loaded, player, False)
        started = True
        #Check if player has loaded from a save state. If not, start new game

        if not loaded1 and freshStart:
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


        elif loaded1 and freshStart: # Load game state if loaded from save
            player, wendigo, cultist, newWorld = load_game_state('save.pkl')
            locations = newWorld['locations'] # Load location data 
            events = newWorld['events'] # Load event data
            dialogue = newWorld['dialogue'] # Load dialogue data
            items = newWorld['items'] # Load item data
            current_location = get_location(newWorld['current_location'], locations) # Get initial location
            
                
        loaded = True
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
                    time.sleep(2)
                    flag = True
                    break

                #Read commands for movement, pause, item use, etc.

                elif command[0] in ['pause', 'menu','start','options']: # Open game menu
                    loaded1, loaded2 = mainMenu(wendigo, cultist, world, loaded, player)

                    if loaded1:
              
                        player, wendigo, cultist, newWorld = load_game_state('save.pkl')
                        locations = newWorld['locations'] # Load location data 
                        events = newWorld['events'] # Load event data
                        dialogue = newWorld['dialogue'] # Load dialogue data
                        items = newWorld['items'] # Load item data
                        current_location = get_location(newWorld['current_location'], locations) # Get initial location

                
                elif command[0] == 'inventory': # Show player inventory
                    player.showInventory()
                    input("\nPress enter to continue...")


                elif command[0] in ['move', 'go', 'walk', 'travel','run', 'n', 'e', 'w', 's']: # Move player to a new location
                    

                    if command[0] in ['n', 'e', 'w', 's']: # filter input for json requests

                        newcommand = comDict[command[0]]

                    else:
                        newcommand = command[1]
                    
                    current_location, moved = move_player(newcommand, current_location, locations, player.getInventory())
                    world['current_location'] = current_location['id']

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
