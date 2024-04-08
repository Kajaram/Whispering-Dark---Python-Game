from Objects.Character import Character

class Wendigo(Character):
    
    def wendigo(self):
        self.setStrength(40)
        self.setCustomName('Wendigo')
        self.playerName = 'wendigo'
        self.setHealth(200)
        self.addToInventory('Diamond Heart')
