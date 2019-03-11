import os
import sys
import random



def fight(enemyName,playerName,HP,enemyHP,mana,attack,enemyAttack,defence,enemyDefence,magicAttack,speed,enemySpeed,enemyMana,enemyMagicAttack,weapon,enemyWeapon):
    defCounter = 0
    enemyDefCounter = 0
    while HP > 0 and enemyHP >0:
        valid = False
        print("\n\n\n******************************")
        print(playerName,"- HP:"+str(HP))
        print(enemyName,"- HP:"+str(enemyHP))

        print("******************************")

        #if your speed is higher than the enemy's speed
        if speed > enemySpeed:
            while valid == False:
                userchoice=input("Attack (a) or Increase Defence (d)? -->")
                print("\n")
                if userchoice == 'a':
                    damage = round(attack-enemyDefence+random.randint(1,2)*2.2)
                    enemyHP = enemyHP - damage
                    print("Inflicted",damage,"harm to enemy!")
                    valid = True

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


            
            enemychoice= random.randint(1,2)

            
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

            
    #if enemy speed greater
        else:
            enemychoice= random.randint(1,2)

            if enemychoice == 1:
                enemyDamage = round(enemyAttack-defence+random.randint(1,2)*2.2)
                HP = HP - enemyDamage

            elif enemychoice == 2:
                if enemyDefCounter <=3:
                    enemyDefence= enemyDefence + 0.5
                    enemyDefCounter = enemyDefCounter+1
                else:
                    enemyDefCounter = enemyDefCounter+1



            while valid == False:
                userchoice=input("Attack (a) or Defensive move (d)? -->")
                print("\n")
                if userchoice == 'a':
                    damage = round(attack-enemyDefence+random.randint(1,2)*2.2)
                    enemyHP = enemyHP - damage
                    valid = True


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
                
            if HP > 0:
                if userchoice == 'a':
                    print("Inflicted",damage,"harm to enemy!")
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
