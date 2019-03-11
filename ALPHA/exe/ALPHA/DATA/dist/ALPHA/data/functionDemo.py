import os
import sys
import random



def fight(enemyName,playerName,HP,enemyHP,mana,attack,enemyAttack,defence,enemyDefence,magicAttack,speed,enemySpeed,enemyMana,enemyMagicAttack,weapon,enemyWeapon):
    defCounter = 0
    enemyDefCounter = 0
    while HP > 0 and enemyHP >0:
        valid = False
        print("\n\n\n******************************")
        print(playerName,"- HP:"+str(HP),"Mana:"+str(mana))
        print(enemyName,"- HP:"+str(enemyHP),"Mana:"+str(enemyMana))

        print("******************************")

        #if your speed is higher than the enemy's speed
        if speed > enemySpeed:
            while valid == False:
                userchoice=input("Attack (a), Magic (m)(2 mana cost) or Increase Defence (d)? -->")
                print("\n")
                if userchoice == 'a':
                    damage = round(attack-enemyDefence+random.randint(1,2)*2.2)
                    enemyHP = enemyHP - damage
                    print("Inflicted",damage,"harm to enemy!")
                    valid = True

                elif userchoice == 'm':
                    print("\nWhich magic will you use?")
                    print("Speed UP^^ (s)")
                    print("Defence UP^^ (d)")
                    print("Water Spear (a)")
                    print("[BACK] (b)")
                    magicChoice = input("-->")
                    if magicChoice == 'a':
                        damage = round(magicAttack-enemyDefence+random.randint(1,2)*2.2)
                        enemyHP = enemyHP - damage
                        print("Inflicted",damage,"harm to enemy!")
                        valid=True
                    elif magicChoice == 's':
                        speed = speed+1
                        print("Speed increased!")
                        valid=True
                    elif magicChoice == 'd':
                        if defCounter <=3:
                            defence= defence + 1.25
                            defCounter = defCounter+1
                            print("Magic surrounds your body- defence increased!")
                        else:
                            print("You try to magically defend yourself... but you fail!")
                        valid=True
                    elif magicChoice == 'b':
                        print("Back...\n")
                    mana=mana-2

                elif userchoice == 'd':
                    if defCounter <= 3:
                        defCounter = defCounter + 1
                        defence= defence + 0.5
                        print("You brace yourself- defence increased!")
                    else:
                        print("You try to brace yourself... but fail!")
                    valid=True
                    
                else:
                    print("Invalid Input! Try again!")


            
            enemychoice= random.randint(1,3)

            
            if enemychoice == 1:
                damage = round(enemyAttack-defence+random.randint(1,2)*2.2)
                HP = HP - enemyDamage
                print("**The enemy inflicted",enemyDamage,"harm to you!**\n")

            elif enemychoice == 2:
                if enemyDefCounter <= 3:
                    enemyDefence= enemyDefence + 0.5
                    print("**The enemy braces themselves- their defence increased!**")
                    enemyDefCounter = enemyDefCounter +1
                else:
                    print("**The enemy tries to brace themself... but fails!**")

            elif enemychoice == 3:
                enemyMagicChoice = random.randint(1,3)
                if enemyMagicChoice == 1:
                    enemyDamage = round(enemyMagicAttack-defence+random.randint(1,2)*2.2)
                    HP = HP - enemyDamage
                    print("**Enemy used a spell and inflicted",enemyDamage,"harm to you!**")
                elif enemyMagicChoice == 2:
                    enemySpeed = enemySpeed+1
                    print("**Enemy's speed increased magically!**")
                elif enemyMagicChoice == 3:
                    if enemyDefCounter <=3:
                        enemyDefence= enemyDefence + 1.25
                        print("**Magic surrounds the enemy's body- enemy defence increased!**")
                    else:
                        print("**The enemy tries to defend themself magically... but fails!**")
                enemyMana=enemyMana-2
            
    #if enemy speed greater
        else:
            enemychoice= random.randint(1,3)

            if enemychoice == 1:
                enemyDamage = round(enemyAttack-defence+random.randint(1,2)*2.2)
                HP = HP - enemyDamage

            elif enemychoice == 2:
                if enemyDefCounter <=3:
                    enemyDefence= enemyDefence + 0.5
                    enemyDefCounter = enemyDefCounter+1
                else:
                    enemyDefCounter = enemyDefCounter+1


            elif enemychoice == 3:
                enemyMagicChoice = random.randint(1,3)
                if enemyMagicChoice == 1:
                    enemyDamage = round(enemyMagicAttack-defence+random.randint(1,2)*2.2)
                    HP = HP - enemyDamage
                elif enemyMagicChoice == 2:
                    enemySpeed = enemySpeed+1
                elif enemyMagicChoice == 3:
                    if enemyDefCounter <=3:
                        enemyDefence= enemyDefence + 1.25
                        enemyDefCounter = enemyDefCounter+1
                    else:
                        enemyDefCounter = enemyDefCounter+1
                enemyMana=enemyMana-2

            while valid == False:
                userchoice=input("Attack (a), Magic (m)(2 mana cost) or Defensive move (d)? -->")
                print("\n")
                if userchoice == 'a':
                    damage = round(attack-enemyDefence+random.randint(1,2)*2.2)
                    enemyHP = enemyHP - damage
                    valid = True

                elif userchoice == 'm':
                    print("\nWhich magic will you use?")
                    print("Speed UP^^ (s)")
                    print("Defence UP^^ (d)")
                    print("Water Spear (a)")
                    print("[BACK] (b)")
                    magicChoice = input("-->")
                    if magicChoice == 'a':
                        damage = round(magicAttack-enemyDefence+random.randint(1,2)*2.2)
                        enemyHP = enemyHP - damage
                        valid=True
                    elif magicChoice == 's':
                        speed = speed+1
                        print("Speed increased!")
                        valid=True
                    elif magicChoice == 'd':
                        if defCounter <=3:
                            defence= defence + 1.25
                            defCounter=defCounter+1
                        else:
                            defCounter=defCounter+1
                        valid=True
                    elif magicChoice == 'b':
                        print("Back...\n")
                    mana=mana-2

                elif userchoice == 'd':
                    if defCounter <=3:
                        defence= defence + 0.5
                        defCounter = defCounter+1
                    else:
                        defCounter = defCounter+1
                    valid=True

                else:
                    print("Invalid Input! Try again!")


            if enemyHP > 0:
                if enemychoice == 1:
                    print("**The enemy inflicted",enemyDamage,"harm to you!**")

                elif enemychoice == 2:
                    if enemyDefCounter <=3:
                        print("**The enemy braces themselves- their defence increased!**")
                    else:
                        print("**The enemy tries to brace themself... but fails!**")
                
                elif enemychoice == 3:
                    if enemyMagicChoice == 1:
                        print("**Enemy used a spell and inflicted",enemyDamage,"harm to you!**")
                    elif enemyMagicChoice == 2:
                        print("**Enemy's speed magically increased!**")
                    elif enemyMagicChoice == 3:
                        if enemyDefCounter <=3:
                            print("**Magic surrounds the enemy's body- enemy defence increased!**")
                        else:
                            print("**The enemy tries to defend themselves magically... but fails!**")
            if HP > 0:
                if userchoice == 'a':
                    print("Inflicted",damage,"harm to enemy!")
                elif userchoice == 'm':
                    if magicChoice == 'a':
                        print("Inflicted",damage,"harm to enemy!")
                    elif magicChoice == 's':
                        speed = speed+1
                        print("Speed increased!")
                    elif magicChoice == 'd':
                        if defCounter <=3:
                            print("Magic surrounds your body- defence increased!")
                        else:
                            print("You try to defend yourself magically... but fail!")
                elif userchoice == 'd':
                    if defCounter<=3:
                        print("You brace yourself- defence increased!")
                    else:
                        print("You try to brace yourself... but fail!")




    if HP > enemyHP:
        print("Battle Won! Congratulations!")
        input("...")
        won = True

    else:
        print("You were defeated!")
        input("...")
        won = False

    return won
