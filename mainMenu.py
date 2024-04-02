# mainMenu.py
import json

# Save Function
def save_game(game_state, filename='savegame.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Game saved successfully!")
    except IOError as e:
        print(f"An error occurred while saving the game: {e}")

# Load Function
def load_game(filename='savegame.json'):
    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
        print("Game loaded successfully!")
        return game_state
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
    except json.JSONDecodeError:
        print("Save file is corrupted.")

# Function to gather the current game state
# This is a placeholder, you need to implement this according to your game's logic
def get_current_game_state():
    return {
        # ... your game state data ...
    }

# Function to initialize a new game state
# This is a placeholder, you need to implement this according to your game's logic
def initialize_new_game_state():
    return {
        # ... your initial game state data ...
    }

# Main Menu Logic
def main_menu():
    # Placeholder for menu logic
    pass

# Show Menu and Handle User Input
def handle_menu():
    print("1. Save Game")
    print("2. Load Game")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        current_game_state = get_current_game_state()
        save_game(current_game_state)
    elif choice == '2':
        game_state = load_game()
        if game_state:
            # Here you would update your game's current state
            # with the loaded state. This might involve updating
            # the game's internal variables, restarting the game loop, etc.
            pass

# Run the main menu
if __name__ == "__main__":
    while True:
        main_menu()
        handle_menu()
