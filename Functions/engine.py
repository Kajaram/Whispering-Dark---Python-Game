import json 
import Functions.inventoryFunctions as inventoryFunctions

# Load game data from JSON
def load_game_data(filename, param):
    with open(filename, 'r') as file:
        game_data = json.load(file)
    return game_data[param]

# Find a location by ID
def get_location(location_id, locations):
    for location in locations:
        if location['id'] == location_id:
            return location
    return None

# Display current location details
def describe_location(location):
    print("\n Current location: " + location['name'])
    print(location['description'])

    # for direction, destination_id in location.get('exits', {}).items():
    #     destination = get_location(destination_id, locations)
    #     if destination:
    #         print(f"To the {direction} is {destination['name']}.")


def check_event_happened(event_id, game_data):
    for event in game_data:
        if event["id"] == event_id:
            return event["happened"]
    return None

def set_event_happened(event_id, game_data):
    for event in game_data:
        if event["id"] == event_id:
            event["happened"] = True
    return None
    