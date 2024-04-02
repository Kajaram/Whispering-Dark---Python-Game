# save_system.py
import json

def save_game(game_state, filename='savegame.json'):
    """Save the current state of the game to a file."""
    try:
        with open(filename, 'w') as f:
            json.dump(game_state, f)
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
        return None  # Or return your initial game state
    except json.JSONDecodeError:
        print("Save file is corrupted.")
        return None
