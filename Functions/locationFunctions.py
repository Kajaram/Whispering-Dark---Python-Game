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
