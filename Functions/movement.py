from Functions.locationFunctions import get_location

def move_player(command, current_location, locations):
    if command in current_location.get('exits', {}):
        new_location_id = current_location['exits'][command]
        return get_location(new_location_id, locations), True
    else:
        print("You can't go that way.")
        return current_location, False