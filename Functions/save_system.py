import json
import os  # Make sure to import the os module for file operations

def save_game(game_state, filename='savegame.json'):
    """Save the current state of the game to a file."""
    try:
        with open(filename, 'w') as f: # Open file in write mode
            json.dump(game_state, f)  # Serialize game_state to JSON and write to file
        print("Game saved successfully.")  # Adding a success message for clarity
        return True
    except IOError as e: # Catch IO errors like file write permissions
        print(f"An error occurred while saving the game: {e}")  # Notify user of error
        return False # Return False to indicate failure


def load_game(filename='savegame.json'):
    """Load the game state from a file."""
    try:
        with open(filename, 'r') as f: # Open file in read mode
            game_state = json.load(f)  # Deserialize JSON content to Python object
        return game_state  # Return the game state
    
    except FileNotFoundError:  # Catch if the file does not exist
        print("No save file found.") # Notify user, treat as new game
        return False  # Return None to indicate no data
    
    except json.JSONDecodeError: # Catch JSON errors
        print("Save file is corrupted.")  # Notify user of corrupt save
        return None # Return None to indicate error


def delete_save():
    try:
        os.remove('savegame.json') # Attempt to remove the save file
        return True  # Return True to indicate success
    
    except FileNotFoundError: # Catch if the file does not exist
        return False # Return False, no file to delete
    
    except Exception as e: # Catch all other exceptions
        print(f"An error occurred: {e}") # Notify user of error
        return False  # Return False to indicate failure
    
def update_state(player, wendigo, cultist, events, locations, current_location, current_location_id):
    game = load_game()
    player.from_dict(game["player"])
    wendigo.from_dict(game["wendigo"])
    cultist.from_dict(game["cultist"])
    events.from_dict(game["events"])
    locations.from_dict(game[locations])
    current_location.from_dict(game["cultist"])
    locations = game['locations']
    current_location.from_dict(game[current_location_id])