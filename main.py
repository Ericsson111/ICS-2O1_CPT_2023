from InputExtensions import *
from Colors import *
import time 
import random 

random.seed()
# Asks player for their name 
#playerName = input("Elder: Brave traveler! What is thy name? ")

# Display Welcome Message to the Player
#print("Elder: Welcome " + playerName + "!\n\tTo the enchanting realm of Elysium!\n\tPrepare to embark on a thrilling adventure where danger lurks at every turn.\n\tBrace yourself for an extraordinary journey into the unknown.\n")
print("-"*75)

# Game Status 
gameOnGoing = True 
currentLocation = "Village"
battleOnGoing = True
shopOnGoing = True 

# Player Status 
playerHealthPoint = 100 
playerElysiumShards = 2000
playerExperienceLevel = 65
playerKillCount = 0

# Player Inventory
playerWeapon = "Wooden Sword"
playerArmour = "Leather Armour"
playerPotion = "Healing Potion"
playerAbility = "Fire"

# Map
gameMap = {"Village": {"n": "Treasure Room", "e": "Forest"},
           "Cave": {"w": "Treasure Room", "s": "South"},
           "Forest": {"n": "Cave", "w": "Village"},
           "Treasure Room": {"s": "Village", 'e': "Cave"}}
           
def displayGameMap():
    print(colors.fg.yellow + "-----------Map-----------")
    if currentLocation == "Village":
        print("| Treasure Room\t Cave   |\n|\t\t        |") 
        print("|\t\t        |\n|    Village\tForest  |\n|\tX\t\t|")
    elif currentLocation == "Treasure Room":
        print("| Treasure Room\t Cave   |\n|\tX\t        |") 
        print("|\t\t        |\n|    Village\tForest  |\n|\t\t\t|")
    elif currentLocation == "Cave":
        print("| Treasure Room\t Cave   |\n|\t\t  X     |") 
        print("|\t\t        |\n|    Village\tForest  |\n|\t\t\t|")
    elif currentLocation == "Forest":
        print("| Treasure Room\t Cave   |\n|\t\t        |") 
        print("|\t\t        |\n|    Village\tForest  |\n|\t\t  X     |")
    print("-"*25)

def exploration(location):
    global currentLocation
    print(colors.fg.yellow + "You are current at the " + currentLocation)
    npcDialogue()
    displayGameMap()
    while True:
        travelDirection = inputTravelDirection() # Validate travelling direction
        if travelDirection in [direction for direction in gameMap[currentLocation].keys()]:
            secretNumber = random.randint(1, 10)
            if random.randint(1, 10) == secretNumber: # 1/100 Chance to Fight
                currentLocation = gameMap[location][travelDirection] # Modify player's current location 
                print("You are currently at the " + currentLocation + "!" + colors.reset)
                combat() 
            else:
                currentLocation = gameMap[location][travelDirection] # Modify player's current location 
                print("You are currently at the " + currentLocation + "!" + colors.reset)
                break
        else:
            print(colors.fg.red + "(Forgotten Forest is Unreachable)" + colors.reset)
            
    if currentLocation == "Treasure Room": # Fighting occurs 100% in Treasure room
        print(colors.reset + "-" * 75)
        combat()
    
def playerInventory():
    print(colors.fg.cyan + "-"*27)
    print("Player Inventory:")
    print("Weapon: " + playerWeapon)
    print("Armour: " + playerArmour)
    print("Potion: " + playerPotion)
    print("Ability: " + playerAbility)
    print("-"*27 + colors.reset)
    
def playerStatus():
    print(colors.fg.cyan + "-"*27)
    print("Player Status:")
    print("Health Point: " + str(round(playerHealthPoint, 2)))
    print("Elysium Shards: " + str(playerElysiumShards))
    print("Experience Level: " + str(playerExperienceLevel))
    print("Kill Count: " + str(playerKillCount))
    print("-"*27 + colors.reset)
    
playerSleepCountDown = 3
def playerRest(): # Sleep
    global playerSleepCountDown, playerHealthPoint
    if currentLocation == "Treasure Room":
        print(colors.fg.red + "You cannot rest in the Treasure Room!")
        print("It is unsafe to spend overnight." + colors.reset)
    else:
        while playerSleepCountDown > 0:
            print(colors.fg.yellow + "Sleeping... " + str(playerSleepCountDown))
            time.sleep(1)
            playerSleepCountDown -= 1 
        playerHealthPoint = 100 # Regenerate all the health
        print(colors.reset)
    
#################################### Combat #################################### 
gameInventory = {"weapon": {"Wooden Sword": 14, "Iron Sword": 20, "Gold Sword": 29},
              "potion": {"Healing Potion": 30, "Poison Potion": 20, "Zap": 15},
              "armour": {"Leather Armour": 0.85, "Iron Armour": 0.67, "Gold Armour": 0.5},
              "ability": {"Fire": 25, "Lightning": 30}}
              
def checkBattleStatus(Health, Damage, Attacker): # Check if enemy is dead
    global battleOnGoing
    if Damage >= Health: 
        if Attacker == playerName:
            battleOnGoing = False
            return "Victory!"
        else:
            battleOnGoing = False
            return "You Died!"
    else:
        return False 
        
def combatAttack(enemy): # Player Attacking
    global playerHealthPoint, combatEnemyHealth, playerElysiumShards, playerKillCount
    attackActionDict = {1: "weapon", 2: "potion", 3: "ability"}
    attackItemDict = {"weapon": playerWeapon, "potion": playerPotion, "ability": playerAbility}
    attackAction = inputIntegerBetween("Select your attack action:\n\t1. Sword\n\t2. Potion\n\t3. Ability\n", 1, 3)
    attackAction = attackActionDict[attackAction]
    attackItem = attackItemDict[attackAction]
    if attackItem == "Healing Potion": # Healing
        if playerHealthPoint + 30 >= 100:
            playerHealthPoint = 100
            print(colors.fg.yellow + "You have recovered your health to 100")
        else:
            playerHealthPoint += 30
            print(colors.fg.yellow + "You have recovered your health to " + str(round(playerHealthPoint, 2)))
            
    else: # Attacking
        playerDamage = gameInventory[attackAction][attackItem] 
        battleStatus = checkBattleStatus(combatEnemyHealth, playerDamage, playerName)
        if battleStatus == False: # Battle On Going
            combatEnemyHealth -= playerDamage
            print(colors.fg.yellow + "The enemy has dealt " + str(playerDamage) + " damage!")
            print(colors.reset)
            print("Player Health: " + str(round(playerHealthPoint, 2)) + " Enemy Health: " + str(combatEnemyHealth))
            print("Continue Attacking!")
            combatDefend(enemy)
        else: # Battle Ends
            battleOnGoing = False
            print(colors.fg.yellow + "The enemy has dealt " + str(playerDamage) + " damage!")
            print(colors.reset)
            print("Player Health: " + str(round(playerHealthPoint, 2)) + " Enemy Health: 0")
            if playerHealthPoint > 0:
                print("Player Health: " + str(round(playerHealthPoint, 2)))
                print(colors.fg.yellow + battleStatus + "!")
                print("You earned 50 Elysium Shards" + colors.reset)
                playerKillCount += 1
                playerElysiumShards += 50
            else:
                print(colors.fg.red + "You Died" + colors.reset)
                playerKillCount = 0 
                playerElysiumShards = 0 

enemyHealthLibrary = {"Vampire": 105, "Skeleton": 71, "Snake": 85, "Bandit": 87, "Dark Knight": 100}
enemyDamageLibrary = {"Vampire": 19, "Skeleton": 12, "Snake": 16, "Bandit": 13, "Dark Knight": 23}

combatEnemyHealth = None

def combatEnemy():
    global combatEnemyHealth
    enemyID = random.randint(0, 4)
    enemy = [enemy for enemy in enemyHealthLibrary.keys()][enemyID]
    combatEnemyHealth = enemyHealthLibrary[enemy]
    print(colors.fg.yellow + "(Your enemy is " + enemy + ": " + str(combatEnemyHealth) + " Health)" + colors.reset)
    return enemy

def combatDefend(enemy): # Enemy Attacking 
    global playerHealthPoint, playerElysiumShards, playerKillCount
    # gameInventory["armour"][playerArmour] is the discounted damage the player recieve with armour
    enemyDamage = round(enemyDamageLibrary[enemy] * gameInventory["armour"][playerArmour], 2)
    battleStatus = checkBattleStatus(playerHealthPoint, enemyDamage, enemy)
    if battleStatus == False:
        playerHealthPoint -= round(enemyDamage, 2)
        print(colors.fg.yellow + "You have dealt " + str(enemyDamage) + " damage!")
        print(colors.reset)
        print("Player Health: " + str(round(playerHealthPoint, 2)))
        print("Hold on in the battle!\n")
        combatAttack(enemy)
    else: # Battle Ends
        battleOnGoing = False
        print(colors.fg.yellow + "You have dealt " + str(enemyDamage) + " damage!")
        print(colors.reset)
        if playerHealthPoint > 0:
            print("Player Health: " + str(round(playerHealthPoint, 2)))
            print(colors.fg.yellow + battleStatus + "!")
            print("You earned 50 Elysium Shards" + colors.reset)
            playerKillCount += 1
            playerElysiumShards += 50
        else:
            print(colors.fg.red + "You Died" + colors.reset)
            playerKillCount = 0 
            playerElysiumShards = 0 
       
def combatEscape():
    print(colors.fg.lightgreen + "You ran away...")
    print(colors.fg.yellow + "(Everyone in the village is laughing at you)" + colors.reset)
    battleOnGoing = False
    print("-"*75)
    return mainMenu()
    
def combat():
    enemy = combatEnemy()
    while battleOnGoing:
        print(colors.reset)
        combatAction = inputIntegerBetween("Select your combat option:\n\t1. Attack\n\t2. Defend\n\t3. Ran Away\n", 1, 3)
        if combatAction == 1:
            combatAttack(enemy)
        elif combatAction == 2:
            combatDefend(enemy)
        elif combatAction == 3:
            combatEscape() 
            
#################################### Shop #################################### 

shopItems = {"weapon": {"Iron Sword": 300, "Gold Sword": 550},
             "potion": {"Healing Potion": 100, "Posion Potion": 100, "Lightning": 100},
             "armour": {"Iron Armour": 370, "Gold Armour": 600},
             "ability": {"Lightning": 500}}
             
def shopPurchase():
    global playerElysiumShards, shopOnGoing
    shopCategory = {1: 'weapon', 2: 'potion', 3: 'armour', 4: 'ability'}
    print(colors.reset)
    
    while shopOnGoing:
        purchaseCategory = inputIntegerBetween("What category are you interested in purchasing today\n\t1. Weapon\n\t2. Potion\n\t3. Armour\n\t4. Ability\n", 1, 4)
        categoryItems = shopItems[shopCategory[purchaseCategory]] # Dictionary of the selected key 
        print(colors.fg.orange + "Item:\t\tPrice:")
    
        for item, price in categoryItems.items():
            print(item + "\t" + str(price))
        
        while shopOnGoing:
            purchaseItem = input(colors.fg.yellow + "What item do you wish to purchase? ")
            if purchaseItem.lower().strip() in [item.lower() for item in categoryItems.keys()]:
                itemValue = categoryItems[purchaseItem.title()]
                if playerElysiumShards >= itemValue:
                    print(colors.fg.green + "Purchase Successful!")
                    print('You now own "' + purchaseItem.title() + '"!')
                    print(colors.reset)
                    category = shopCategory[purchaseCategory]
                    if category == "weapon":
                        playerWeapon = purchaseItem.title()
                    elif category == "potion":
                        playerPotion = purchaseItem.title()
                    elif category == "armour":
                        playerArmour = purchaseItem.title()
                    elif category == "ability":
                        playerAbility = purchaseItem.title()
                        
                    playerElysiumShards -= itemValue 
                    
                    continueBuying = obtainYesNo("Do you wish to continue the purchase?\n(Your current balance is: " + str(playerElysiumShards) + " Elysium Shards")
                    if continueBuying == 'n':
                        shopOnGoing = False 
                        return mainMenu
                    if continueBuying == 'y':
                        return shopPurchase()
                else:
                    print(colors.bg.red + "You do not have enough elysium shards to purchase this item.")
            if purchaseItem.lower().strip() in ['quit', 'q']:
                break
            else:
                print(colors.fg.red + "Please provide valid response.")
                print(colors.reset)
                


#################################### NPC Dialogue #################################### 

npcDialogueDict = {"Villeger": {"Hey traveller!": ["Hey what's up?", "Hey Villager"], "How are you?": ["I'm good!", "Great! How are you?"]},
               "Caveman": {"Unga bunga!": ["hmmm, I wonder what they are saying", "What is he trying to tell me?"],
                           "No understand": ["Maybe I should teach them how to communicate with other", "*Sigh anyways..."]},
               "Elder": {"Young traveller, remember to always listen to the whispers of the wind.": ["Surely", "Well Said"],
                         "May the spirits of the land protect you on your expedition and may you return with tales to inspire generations to come.": ["I won't let them down", "Their spirits will guide me."],
               },
               "Black Smith": {"Ah, a traveler seeking adventure! Remember, a well-made weapon is your truest companion.": ["I'll forge my path with a trusty weapon by my side.", "I won't underestimate the power of a well-crafted blade on my journey."],
                               "A word of advice, traveler: Don't underestimate the value of a sturdy shield.": ["I'll keep a sturdy shield close, for both defense and peace of mind.", "A sturdy shield shall be my steadfast guardian against any threat."]
               }} 

def npcDialogue():
    npcSpeakerID = random.randint(0, 3)
    npcSpeaker = [person for person in npcDialogueDict.keys()][npcSpeakerID]
    speakerMessage = [message for message in npcDialogueDict[npcSpeaker]][random.randint(0, 1)]
    print(colors.fg.yellow + npcSpeaker + ": " + speakerMessage)
    playerResponse = inputIntegerBetween(colors.reset + "Response:\n\t" + "1. " + npcDialogueDict[npcSpeaker][speakerMessage][0] + "\n\t2. " + npcDialogueDict[npcSpeaker][speakerMessage][1] + "\n\t3. (Leave)\n", 1, 3)
    if playerResponse == 1:
        print(npcDialogueDict[npcSpeaker][speakerMessage][0])
    elif playerResponse == 2:
        print(npcDialogueDict[npcSpeaker][speakerMessage][1])
    elif playerResponse == 3:
        print(colors.fg.yellow + "(You left without saying a word...)\n" + colors.reset)
    # Talk until player decide to leave
def mathQuiz():
    global playerElysiumShards
    total_question = 5
    question_count = 1
    correct_count = 0
    while question_count <= total_question:
        # Generate random integers 
        first_number = random.randint(-10, 10) 
        second_number = random.randint(-10, 10) 
        
        # Choose between addition and subtraction
        operation = random.randint(1, 3) 
        operation_symbol = ''
        
        if operation == 1:
        # Correct Result 
            result = first_number + second_number
            operation_symbol = "+"
        elif operation == 2:
            result = first_number - second_number 
            operation_symbol = "-"
        elif operation == 3:
            result = first_number * second_number 
            operation_symbol = "x"
        
        # Display Question 
        print("Question " + str(question_count) + ": " + str(first_number), operation_symbol, str(second_number))
        
        # User's Response
        userInput = inputFloat("What is your answer: ")
        userInput = round(userInput, 2)
        
        # Count 
        question_count += 1
        
        # Determine User's Response
        if userInput == result:
            correct_count += 1 
            print("Correct")
        elif userInput != result:
            print("Incorrect")
    if correct_count == total_question:
        print(colors.fg.yellow + "Congratulations You have got 100%!")
        print("You have earned 100 Elysium Shards." + colors.reset)
        playerElysiumShards += 100 
    else:
        print(colors.fg.yellow + "You got %d/%d." % (correct_count, total_question))
        print("You have earned 20 Elysium Shards.")
        playerElysiumShards += 20
        print("Better Luck Next Time." + colors.reset)
 
def mainMenu():        
    while gameOnGoing:
        menuOption = inputIntegerBetween("Select your menu option: \n\t1. Explore\n\t2. Check Status\n\t3. Check Inventory\n\t4. Shop\n\t5. Rest\n\t6. Fight\n\t7. Villager Interaction\n\t8. Math Quiz\n\t9. Quit\n", 1, 9)
        if menuOption == 1:
            exploration(currentLocation)
        elif menuOption == 2:
            playerStatus()
        elif menuOption == 3:
            playerInventory()
        elif menuOption == 4:
            shopPurchase()
        elif menuOption == 5:
            playerRest()
        elif menuOption == 6:
            combat()
        elif menuOption == 7:
            npcDialogue()
        elif menuOption == 8:
            mathQuiz()
        elif menuOption == 9:
            print(colors.fg.yellow + "Elder: Good bye, young traveller..")
            print("Elder: It's unfortunate you couldn't stay with us")
            print("Elder: Hopefully you return one day")
            print("Elder: Farewell my friend...")
            quit()
        print("-"*75)
mainMenu()
