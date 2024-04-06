import os
from Functions.save_system import delete_save, save_game, load_game
from Functions.engine import get_location
from Functions.centerprint import centered_print

def mainMenu(player, locations, wendigo, cultist, events, current_location, loaded=False, started=False) :
    #current game state
    game_state = {

                    "player": player.to_dict(),
                    "wendigo": wendigo.to_dict(),
                    "cultist": cultist.to_dict(),
                    "events": events,  
                    "locations": locations,
                    "current_location_id": current_location['id'],
                }
    
    while True:

        #clear the console and prompt user for 
        os.system('cls' if os.name == 'nt' else 'clear')
        title = ''
        centered_print(f"\n            WHISPERING DARK\n\n                 MENU.")
        centered_print("\n      For a new game, type 'new'." if not loaded and not started else "")
        centered_print("\n   To save your game, type 'save'.\n\n To load your previous game, type 'load'.\n\n To delete your save data, type 'delete'.\n\n       To resume, type 'resume'\n")
        action = input("\n").strip().lower()
        
        if action == 'new':  # Indicate a new game should be started
            return False
        
        elif action == 'load':
             
            loaded_state = load_game('savegame.json')

            if loaded_state: # Update game state with loaded data
                player.from_dict(loaded_state["player"])
                current_location = get_location(loaded_state["current_location_id"], locations)
                print("Game loaded successfully.")
                input("\nPress enter to continue...")
                return True # Indicate game has been loaded
            
            else:
                input("\nPress enter to continue...")
                return False # Failed to load, start a new game

        elif action == 'save':
                # Attempt to save the game
                if save_game(game_state, 'savegame.json'):
                    input("\nPress enter to continue...")
                else:
                    print("\nFailed to save game.")
                    input("\nPress enter to continue...")
                return False

        elif action == 'delete': # Delete save data
            delete_save()
            input("\nPress enter to continue...")

        elif action == 'resume':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            input("Unrecognized command, press enter...")