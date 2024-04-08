from Objects.Cultist import Cultist
from Objects.Wendigo import Wendigo
from Objects.player import Player

class characterFactory:
    
    def makeCharacter(self, breed, name=""):

        if breed == 'cultist':
            cultist = Cultist()
            cultist.cultist()
            return cultist
        
        elif breed == 'wendigo':
            wendigo = Wendigo()
            wendigo.wendigo()
            return wendigo
        
        elif breed == 'player':
            player = Player()
            player.player(name)
            return player
        

