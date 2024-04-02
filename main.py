from Functions.engine import load_game_data, get_location, describe_location, move_player
from intro import introSequence
from mainMenu import Menu

locations = load_game_data('Whispering-Dark Updated.json')  # Adjust the path as necessary
current_location = get_location('cabin', locations)  # Starting location

# Main game loop
if __name__ == '__main__':
    
    # mainMenu()
    introSequence()

    locations = load_game_data('Whispering-Dark Updated.json')  # Adjust the path as necessary
    current_location = get_location('cabin', locations)  # Starting location
    
    print("Welcome to Whispering Dark. Type 'quit' to exit at any time.")

    while True:

        describe_location(current_location)
        command = input("\nWhat do you want to do? ").strip().lower()
        
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