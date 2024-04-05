import json
import os  # Make sure to import the os module for file operations

def save_game(game_state, filename='savegame.json'):
    """Save the current state of the game to a file."""
    try:
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Game saved successfully.")  # Adding a success message for clarity
        return True
    except IOError as e:
        print(f"An error occurred while saving the game: {e}")
        return False

def load_game(filename='savegame.json'):
    """Load the game state from a file."""
    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
        return game_state
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None
    except json.JSONDecodeError:
        print("Save file is corrupted.")
        return None

def delete_save(filename='savegame.json'):
    """Delete the save game file if it exists."""
    try:
        os.remove(filename)
        print("Save file successfully deleted.")  # Inform the user of successful deletion
        return True
    except FileNotFoundError:
        print("No save file found to delete.")
        return False
    except OSError as e:  # Catching any OS error that might occur
        print(f"Error deleting save file: {e}")
        return False
