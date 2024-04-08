from Objects.Character import Character

class Player(Character):
    
    def player(self, name="player"):
        self.setStrength(10)
        self.setCustomName(name)
        self.setHealth(100)
