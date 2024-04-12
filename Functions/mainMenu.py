import os
from Functions.engine import get_location, load_world2
from Functions.centerprint import centered_print
from Functions.newSave import load_game_state, save_game_state, delete_save

def mainMenu(wendigo, cultist, world, loaded, player, started=True) :


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
            return False, True
        
        elif action == 'load':
            if not started:
                return True, True
            else: 
                return True, False
            

        elif action == 'save':
                # Attempt to save the game

                save_game_state(player, wendigo, cultist, world, 'save.pkl')
                input("Press enter to continue..")
                continue


        elif action == 'delete': # Delete save data
            delete_save()
            input("\nPress enter to continue...")
            continue

        elif action == 'resume':
            os.system('cls' if os.name == 'nt' else 'clear')
            loaded = True
            return False, False

        else:
            input("Unrecognized command, press enter...")
            continue

            