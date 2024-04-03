class Character:
    def __init__(self, health, inventory=None):
        self._health = health
        self._inventory = inventory if inventory is not None else []

    def getHealth(self):
        return self._health

    def setHealth(self, new_health):
        self._health = new_health

    def getInventory(self):
        return self._inventory

    def addToInventory(self, item):
        self._inventory.append(item)

    def removeFromInventory(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
        else:
            print("Item not found in inventory!")