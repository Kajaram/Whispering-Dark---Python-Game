from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.inventoryFunctions import pick_up_item, use_item
from Functions.engine import load_game_data,check_event_happened
from Functions.intro import sequence
from Functions.quickTime import timer
from Objects.Character import Character
from Functions.fight import fightFunc
import os
import time
# import sys
# sys.path.append('c:\python312\lib\site-packages')

player = Character(100, 'player')
wendigo = Character(200, 'wendigo', 40)
cultist = Character(40, 'cultist', 30)

evelyn = Character(50)
sophia = Character(100)
rohan = Character(100)
ava = Character(100)
daniel = Character(100)

locations = load_game_data('assets/Whispering-Dark Updated.json', 'locations') 
dialogue = load_game_data('assets/Whispering-Dark Updated.json', 'dialogue') 
items = load_game_data('assets/Whispering-Dark Updated.json', 'items') 
current_location = get_location('cabin', locations) 

# Main game loop
if __name__ == '__main__':

    
    myName = input('\nEnter your Name:')
    print("Welcome,", myName)
    player.setCustomName(myName)

    # menu()
    sequence('intro_cutscene')
 
    
    print("\nWelcome to Whispering Dark. Type 'quit' to exit at any time.")

    while True:

        os.system('cls')
        describe_location(current_location)
        # print(current_location['items'])
        command = input("\nWhat do you want to do?\n").strip().lower()
        command = command.split()
        
        
        if len(command) > 0:
            if command[0] == 'quit':
                print(f"Thanks for playing  {player.getCustomName()}. Goodbye!")
                time.sleep(3)
                # os.system('cls')
                break

            elif command[0] == 'inventory':
                player.showInventory()
                time.sleep(3)

            elif command[0] in ['move', 'go', 'walk', 'travel','run']:
                current_location, moved = move_player(command[1], current_location, locations, player.getInventory())
                
                if not moved:
                    print("You can't move in that direction..")
                    time.sleep(2)
                else:

                    if current_location['id'] == 'trail' and not wendigo.checkIsDead():

                        print("\nThe wendigo emerges from the tree, claws bared. It pounces towards you!")
                        fightFunc(player, wendigo, dialogue, items)
                        
                    elif current_location['id'] == 'church_entrance' and not check_event_happened("church_discovery", locations):
                        sequence('church_discovery')   

                    elif current_location['id'] == 'church_basement' and not cultist.checkIsDead():
                        fightFunc(player, cultist, dialogue, items)
                    

                    else:    
                        continue

                if player.checkIsDead() :
                        print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                        break
        

            elif command[0] in ['grab', 'take', 'equip'] :
                pick_up_item(command[1], player.getInventory(), current_location)

            else:
                print("Unknown command. Please try again.")

        else:
            print("Please enter a command..")
