from Functions.locationFunctions import get_location
from Functions.intro import sequence
import time
import os

class Character:
    def __init__(self):
        self.name = __name__  # Character's identifier or role
        self.playerName = "" # Character's player or character name
        self._health = 0 # Character's health
        self._strength = 0 # Character's strength
        self._inventory = [] # Character's inventory, ensuring it's a list if None is passed
        self.isDead = False # Flag to check if the character is dead
        self.customName = ''  # Custom name for the character

    #returns the characters's current health
    def getHealth(self):
        return self._health 
    
    #Increases or decreases health (used during fight scenes)
    def setHealth(self, new_health): 
        self._health += new_health 

    #returns a list of items in the characters inventory
    def getInventory(self):
        return self._inventory

    #Adds an item to the character's inventory.
    def addToInventory(self, item):
        self._inventory.append(item)

    #Removes an item from the character's inventory if it exists
    def removeFromInventory(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
        else:
            print("Item not found in inventory!")

    def showInventory(self):
        print(f"Items in {self.customName}'s inventory")
        for item in self._inventory:
            print(item)

    def getName(self):
        return self.playerName
    
    def describe(self):
        description = f"{self.getName()}, with a role of {self.role}"
        if self.race:
            description += f"and of {self.race} race."
        else:
            description += "."
        print(description)

    def getStrength(self):
        return self._strength
    
    def checkIsDead(self):
        if self._health <= 0:
            self.isDead = True  
        else:
            self.isDead = False 
        return self.isDead
    
    def setIsDead(self):
        self.isDead = True
    
    def setCustomName(self, newName):
        self.customName = newName

    def getCustomName(self):
        return self.customName
    
    def setStrength(self, strength):
        self.strength = strength

    # Method to serialize character state to a dictionary
    def to_dict(self):
        return {
            "name": self.playerName,
            "health": self._health,
            "strength": self._strength,
            "inventory": self._inventory,
            "isDead": self.isDead,
            "customName": self.customName
        }

    # Method to deserialize character state from a dictionary
    def from_dict(self, data):
        self.playerName = data.get("name", "")
        self._health = data.get("health", 100)
        self._strength = data.get("strength", 10)
        self._inventory = data.get("inventory", [])
        self.isDead = data.get("isDead", False)
        self.customName = data.get("customName", "")

    def drop_item(self, item_name, current_location):
        current_location['items'].append(item_name)
        self.removeFromInventory(item_name)
        print(f"Item Dropped")
        input("\nPress enter...")


    def use_item(self, item_name, current_location, events=''):

        if item_name in self.getInventory():
                # Trigger event outcome here
            if item_name == 'flashlight' and current_location['id'] == 'church entrance':
                print("The flashlight illuminates the inside of the church.\nExpansive murals line its walls, their glistening colours telling tales of both glory and woe.")
                input("Press enter to continue...")
                # Modify location exits or reveal items
            elif item_name == 'walkie' and current_location['id'] == 'radio tower':
                sequence('radio_tower', events)

            elif item_name == 'bandages':
                self.setHealth(15)
                print(f"{self.getCustomName()} used a bandage! \nYour health increases by 15 points")
                print(f"Player health: ", self.getHealth())
                self.removeFromInventory('bandages')
                input("\nPress enter to continue...")

            elif item_name == 'map':
                exits = current_location['exits']
                for key, val in exits.items():
                    print(f"\n{key} --> {val}")
        
                input("\nPress enter to continue...")
            
            else:
                print(f"\nYou use the {item_name}, but nothing happens.")
                input("\nPress enter to continue...")
        else:
            print("\nYou don't have that item.")
            input("\nPress enter to continue...")

    # Example of picking up an item
    def pick_up_item(self, item_name,current_location):
        
        current_location_items = current_location['items']
        if item_name in current_location_items:
            self._inventory.append(item_name)
            current_location_items.remove(item_name)
            print(f"Picked up {item_name}.")

            if item_name == 'talisman':
                os.system('cls')
                print("The talisman grants you additional health.\nYou will now have twice as many health points as you currently have.")
                self.setHealth(2*self.getHealth())
                print(f"Player health: {self.getHealth()}")
            input("\nPress enter to continue...")
        
        elif item_name in self._inventory:
            print(item_name + " is already in your inventory.")
            input("\nPress enter to continue...")

        else:
            print("That item isn't here.")
            input("\nPress enter to continue...")
        
