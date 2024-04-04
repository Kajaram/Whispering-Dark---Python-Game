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
    
