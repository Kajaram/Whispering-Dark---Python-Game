from Objects.Character import Character

class Cultist(Character):
    
    def cultist(self):
        self.setStrength(30)
        self.setCustomName('Cultist')
        self.playerName = 'cultist'
        self.setHealth(30)
        self.addToInventory('Scythe')
