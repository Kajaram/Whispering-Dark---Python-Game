from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.inventoryFunctions import pick_up_item, use_item
from Functions.engine import load_game_data, check_event_happened, set_event_happened
from Functions.intro import sequence
from Functions.quickTime import timer
from Functions.save_system import save_game, load_game, delete_save  # Ensure this function is created or imported correctly
from Objects.Character import Character
from Functions.fight import fightFunc
import os
import time

# Characters initialization
player = Character(100, 'player')
wendigo = Character(200, 'wendigo', 40)
cultist = Character(30, 'cultist', 30)
evelyn = Character(50)
sophia = Character(100)
rohan = Character(100)
ava = Character(100)
daniel = Character(100)

# Game data loading
locations = load_game_data('assets/Whispering-Dark Updated.json', 'locations')
events = load_game_data('assets/Whispering-Dark Updated.json', 'events')
dialogue = load_game_data('assets/Whispering-Dark Updated.json', 'dialogue')
items = load_game_data('assets/Whispering-Dark Updated.json', 'items')
current_location = get_location('cabin', locations)

def delete_save():
    try:
        os.remove('game_save.json')
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Main game loop
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    myName = input('\nEnter your Name: ')
    print("\nWelcome,", myName)
    print("\nWelcome to WHISPERING DARK. Type 'quit' to exit at any time and Type 'save' to save anytime.")
    
    # Extended choice for game start
    choice = input("\nDo you want to start a new game, load an existing one, or delete the save file? (new/load/delete): ").strip().lower()
    if choice == 'load':
        loaded_state = load_game('game_save.json')
        if loaded_state:
            player.from_dict(loaded_state["player"])
            current_location = get_location(loaded_state["current_location_id"], locations)
            print("Game loaded successfully.")
        else:
            print("Failed to load game, starting a new game instead.")
            sequence('intro_cutscene')
    elif choice == 'delete':
        if delete_save():
            print("Save file deleted successfully.")
        else:
            print("No save file to delete.")
        sequence('intro_cutscene')
    else:
        sequence('intro_cutscene')

    print("\nWelcome to Whispering Dark. Type 'quit' to exit at any time.")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        describe_location(current_location)
        command = input("\nWhat do you want to do?\n").strip().lower()
        command = command.split()
        
        if len(command) > 0:
            if command[0] == 'quit':
                print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                time.sleep(3)
                break

            elif command[0] == 'inventory':
                player.showInventory()
                time.sleep(3)

            elif command[0] == 'save':
                game_state = {
                    "player": player.to_dict(),
                    "current_location_id": current_location['id'],
                    # Consider adding more states as needed
                }
                if save_game(game_state, 'game_save.json'):
                    print("Game saved successfully.")
                else:
                    print("Failed to save game.")
                input("Press Enter to continue...")

            elif command[0] == 'load':
                loaded_state = load_game('game_save.json')
                if loaded_state:
                    player.from_dict(loaded_state["player"])
                    current_location = get_location(loaded_state["current_location_id"], locations)
                    print("Game loaded successfully.")
                else:
                    print("Failed to load game.")
                input("Press Enter to continue...")

            elif command[0] in ['move', 'go', 'walk', 'travel','run']:
                current_location, moved = move_player(command[1], current_location, locations, player.getInventory())
                
                if not moved:
                    time.sleep(2)
                else:

                    if current_location['id'] == 'trail' and not wendigo.checkIsDead():
                        
                        sequence('wendigo_confrontation', events, player, wendigo, dialogue, items)
                      
                        

                    elif current_location['id'] == 'church_entrance':

                        sequence('church_discovery', events, player, cultist, dialogue, items)   



                    elif current_location['id'] == 'church_basement' and not cultist.checkIsDead():

                        sequence('basement_confrontation', events, player, cultist, dialogue, items)
                        

                    else:    
                        continue

                if player.checkIsDead() :
                        print(f"Thanks for playing {player.getCustomName()}. Goodbye!")
                        break
        

            elif command[0] in ['grab', 'take', 'equip'] :
                pick_up_item(command[1], player.getInventory(), current_location)

            elif command[0] in ['open', 'unlock', 'read']:
                openItem(current_location, player.getInventory(), command[1])

            else:
                print("Unknown command. Please try again.")

        else:
            print("Please enter a command..")
