import os
from Functions.save_system import delete_save, save_game, load_game
from Functions.engine import get_location

def mainMenu(player, locations, wendigo, cultist, events, current_location) :
    
    game_state = {

                    "player": player.to_dict(),
                    "wendigo": wendigo.to_dict(),
                    "cultist": cultist.to_dict(),
                    "events": events,  
                    "locations": locations,
                    "current_location_id": current_location['id'],
                }
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        action = input("            MENU.\n\nFor a new game, type 'new'.\n\nTo save your game, type 'save'.\n\nTo load your previous game, type 'load'.\n\nTo delete your save data, type 'delete.\n\nTo resume, type 'resume'\n").strip().lower()
        
        if action == 'new':
            return False
        
        elif action == 'load':
             
            loaded_state = load_game('savegame.json')
            if loaded_state:
                player.from_dict(loaded_state["player"])
                current_location = get_location(loaded_state["current_location_id"], locations)
                print("Game loaded successfully.")
                input("\nPress enter to continue...")
                return True
            
            else:
                print("Failed to load game, starting a new game instead.")
                input("\nPress enter to continue...")
                return False

        elif action == 'save':
                
                if save_game(game_state, 'savegame.json'):
                    input("\nPress enter to continue...")
                else:
                    print("\nFailed to save game.")
                    input("\nPress enter to continue...")

        elif action == 'delete':
            delete_save()
            input("\nPress enter to continue...")

        else:
            break