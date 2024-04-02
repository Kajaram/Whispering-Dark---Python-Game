import json 
import Functions.inventoryFunctions as inventoryFunctions

# Load game data from JSON
def load_game_data(filename):
    with open(filename, 'r') as file:
        game_data = json.load(file)
    return game_data['locations']

# Find a location by ID
def get_location(location_id, locations):
    for location in locations:
        if location['id'] == location_id:
            return location
    return None

# Display current location details
def describe_location(location):
    print("\n" + location['name'])
    print(location['description'])

    for direction, destination_id in location.get('exits', {}).items():
        destination = get_location(destination_id, locations)
        if destination:
            print(f"To the {direction} is {destination['name']}.")

# Handle movement commands
def move_player(command, current_location, locations):
    if command in current_location.get('exits', {}):
        new_location_id = current_location['exits'][command]
        return get_location(new_location_id, locations), True
    else:
        print("You can't go that way.")
        return current_location, False
