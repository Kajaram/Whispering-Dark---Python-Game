from Functions.locationFunctions import get_location # Import function to get details of a new location


def move_player(command, current_location, locations, inventory):



    if command in current_location['exits']:
        # Check if the command corresponds to an available exit in the current location
        new_location_id = current_location['exits'][command]  # Get the ID of the new location
        new_location = get_location(new_location_id, locations)


        if new_location['requirement'] in inventory:
              return new_location, True # Return the new location and True indicating successful movement

        else:
            print(new_location['blocked-text'])
            input("\n\nPress enter to continue...")
            return current_location, False
        
    
    else:
        print("You can't move in that direction..") # Indicate an invalid direction command
        input("Press enter to continue...")
        return current_location, False # Return current location and False indicating movement was not successful