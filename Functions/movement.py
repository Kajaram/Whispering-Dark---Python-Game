from Functions.locationFunctions import get_location # Import function to get details of a new location


def move_player(command, current_location, locations, inventory):


    if command == 'n':
        command = 'north'

    elif command == 'e':
        command = 'east'
    
    elif command == 's':
        command = 'south'
    
    elif command == 'w':
        command = 'west'


    if command in current_location['exits']:
        # Check if the command corresponds to an available exit in the current location
        new_location_id = current_location['exits'][command]  # Get the ID of the new location

        if  new_location_id=="church basement" and "basement key" not in inventory:
            # Check if moving to the church basement but the player does not have the basement key
            print("The door is locked.")
            return current_location, False # Return current location and False indicating movement was not successful

        
        elif new_location_id == "church entrance" and "flashlight" not in inventory:
            # Check if moving to the church entrance but the player does not have a flashlight
            print("The path is too dark and treachurous to pass.\nWe need something to light the way..")
            return current_location, False # Return current location and False indicating movement was not successful
        
        elif new_location_id == 'trail' and 'axe' not in inventory:
            # Check if moving to the trail but the player does not have an axe
            print("Whatever took the lives of the other campers was last seen that way...\nI should probably gather more supplies before heading that way.")
            return current_location, False # Return current location and False indicating movement was not successful

        elif command in current_location.get('exits', {}):
             # If the exit is valid and there are no inventory restrictions
            return get_location(new_location_id, locations), True # Return the new location and True indicating successful movement

    
    else:
        print("You can't move in that direction..") # Indicate an invalid direction command
        return current_location, False # Return current location and False indicating movement was not successful