import pickle
import os

def save_game_state(player, wendigo, cultist, world, filename):
    """
    Save the states of the player, wendigo, cultist objects, and the game world.

    Args:
        player: The player object.
        wendigo: The wendigo object.
        cultist: The cultist object.
        world: The game world object containing locations, events, dialogue, and items.
        filename: The filename to save the game state to.
    """
    # Create a dictionary to hold all the objects
    game_state = {
        'player': player,
        'wendigo': wendigo,
        'cultist': cultist,
        'world': world
    }

    # Serialize and save the game state to a file
    try:
        with open(filename, 'wb') as f:
            pickle.dump(game_state, f)
        print("game saved")
        return True
    
    except IOError as e:
        print("Game failed to save")
        return False



def load_game_state(filename):
    """
    Load the saved game state from a file.

    Args:
        filename: The filename from which to load the game state.

    Returns:
        A tuple containing the player, wendigo, cultist objects, and the game world.
    """
    # Initialize variables to hold loaded objects
    player = None
    wendigo = None
    cultist = None
    world = None

    # Load the game state from the file
    with open(filename, 'rb') as f:
        game_state = pickle.load(f)

        # Retrieve player, wendigo, cultist, and world objects from the loaded game state
        player = game_state['player']
        wendigo = game_state['wendigo']
        cultist = game_state['cultist']
        world = game_state['world']

    # Return the loaded objects
    return player, wendigo, cultist, world



def delete_save():
    try:
        os.remove('save.pkl') # Attempt to remove the save file
        return True  # Return True to indicate success
    
    except FileNotFoundError: # Catch if the file does not exist
        print("File not found...")
        return False # Return False, no file to delete
    
    except Exception as e: # Catch all other exceptions
        print(f"An error occurred: {e}") # Notify user of error
        return False  # Return False to indicate failure