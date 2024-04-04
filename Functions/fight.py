from Functions.quickTime import timer
import time
import random
import os

def fightFunc(player, enemy, dialogue, items) :
        
        playerDialogue = dialogue[player.getName()]['fightText']
        enemyDialogue = dialogue[enemy.getName()]['fightText']

        if enemy.checkIsDead():
             return
        
       
        while enemy.getHealth() > 0 and player.getHealth() > 0:
            
            action, answer = timer(7, "\nthink fast!")
            # print(action, answer)
            action = str(action)
            action = action.split()

            if len(action) < 2:
                 print("Command not recognized")
                 continue
            
            weapon = action[1]
            if not answer or weapon not in player.getInventory():
               player.setHealth(-enemy.getStrength())
               os.system('cls')
               print(playerDialogue[random.randint(0,len(playerDialogue)-1)])
               print(f"{enemy.getName()} attacks! You lose {enemy.getStrength()} health!")
               continue

            elif answer:
                weapon = action[1]
                if weapon in player.getInventory():
                    enemy.setHealth(items[weapon]['damage'])
                    os.system('cls')
                    print(enemyDialogue[random.randint(0,len(enemyDialogue)-1)])
                    print(f"You damaged the {enemy.getName()}!")
                    continue

          
        if player.getHealth() > 0:
            print(f"{enemy.getName()} was defeated!")
            enemy.setIsDead()

        else:

            print("\nYOU DIED.\nPlease Try again..")
            time.sleep(2)
            exit
# need to create a damage function inside the player object
# same for enemy object