from quickTime import timer
import random

def fightFunc(enemy, player, currentLocation, locations) :

    if currentLocation == 'trail':

        while enemy.getHealth() > 0 and player.getHealth() > 0:
            
            action, answer = timer(7, "\nthink fast!")
            action.split()

            if action[1] in player.getInventory:
                enemy.setHealth(-locations['items'][action[1]]['damage'])
                print(random.randint(0,locations['fightText']['wendigo']['hurt']))

            if not answer:
               player.setHealth(-40)
               print(random.randint(0,locations['fightText']['player']['hurt']))
               continue

        if player.getHealth > 0:
            print(f"{enemy.getName()} was defeated!")

        else:
            print("\nYOU DIED.\nPlease Try again..")
            exit
# need to create a damage function inside the player object
# same for enemy object