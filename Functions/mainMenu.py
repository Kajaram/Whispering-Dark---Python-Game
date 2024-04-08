import os
from Functions.save_system import delete_save, save_game
from Functions.engine import get_location, load_world2
from Functions.centerprint import centered_print
from Functions.save_system import load_game, save_game

def mainMenu(world, loaded, started=True) :
  
  
    while True:

        #clear the console and prompt user for 
        os.system('cls' if os.name == 'nt' else 'clear')
        title = ''
        centered_print(f"\n            WHISPERING DARK\n\n                 MENU.")
        if not loaded: centered_print("\n      For a new game, type 'new'.")
        centered_print("\n   To save your game, type 'save'.\n\n To load your previous game, type 'load'.\n\n To delete your save data, type 'delete'.")
        if started: centered_print("\n\n       To resume, type 'resume'\n")
        action = input("\n").strip().lower()
        
        if action == 'new':  # Indicate a new game should be started
            centered_print("\nNew Game Started..\n\nPress enter...")
            loaded = True
            return world, False
        
        elif action == 'load':
             
            newWorld = load_world2('savegame.json')
            loaded=True

            if not newWorld:
                input("Game file is empty.. \n\nPress enter")
                continue
                
            else:
                centered_print("Game loaded")
                input("\nPress enter to continue...")
                return newWorld, True
            

        elif action == 'save':
                # Attempt to save the game
                if save_game(world, 'savegame.json'):
                    input("\nPress enter to continue...")
                    continue
                else:
                    print("\nFailed to save game.")
                    input("\nPress enter to continue...")
                    continue

        elif action == 'delete': # Delete save data
            delete_save()
            input("\nPress enter to continue...")
            continue

        elif action == 'resume':
            os.system('cls' if os.name == 'nt' else 'clear')
            loaded = True
            return world, True

        else:
            input("Unrecognized command, press enter...")
            continue

