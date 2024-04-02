from Functions.locationFunctions import get_location, describe_location
from Functions.movement import move_player
from Functions.engine import load_game_data
from Functions.intro import introSequence
from mainMenu import menu
import os

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
        os.system('clear')
        describe_location(current_location)
        command = input("\nWhat do you want to do?\n").strip().lower()
        
        if command == 'quit':
            print("Thanks for playing. Goodbye!")
            break
        elif command in ['north', 'south', 'east', 'west', 'up', 'down']:
            current_location, moved = move_player(command, current_location, locations)
            if not moved:
                print("You can't move in that direction.")

            else:
                continue

        else:
            print("Unknown command. Please try again.")