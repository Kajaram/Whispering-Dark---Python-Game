class Character:
    def __init__(self, health=100, name="", strength = 10, inventory=[]):
        self.name = __name__
        self.playerName = name
        self._health = health
        self._strength = strength
        self._inventory = inventory if inventory is not None else []
        self.isDead = False
        self.customName = ''

    def getHealth(self):
        return self._health 

    def setHealth(self, new_health): 
        self._health += new_health

    def getInventory(self):
        return self._inventory

    def addToInventory(self, item):
        self._inventory.append(item)

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


    
