# challenge 2.py
# Date: 11/12/2014
# Created by: Zach Golik
whichOne = None
takeAway = None
dexterity = 0
strength = 0
health = 0
wisdom = 0
points = 30
choice = None

while points != 0 and choice != 0:
    whichOne = None
    takeAway = None
    choice = int(input('''
                     M E N U
   --------------------------------------------             
    0 - Quit
    1 - Add points to a skill
    2 - Take back points from a skill
    3 - See how many points you have remaining
   --------------------------------------------
   '''))
    if choice == 1:
        while whichOne != 0:
            whichOne = int(input('''
    0 - Quit
    1 - Add points to Dexterity
    2 - Add points to Strength
    3 - Add points to Health
    4 - Add points to Wisdom
    '''))
            if whichOne == 0:
                print("Okay")
            elif whichOne == 1:
                dexPoints = int(input("How many points do you want to add to Dexterity? "))
                if dexPoints <= points:
                    dexterity += dexPoints
                    points = points - dexPoints
                    print("You now have", dexterity, 'dexterity points!')
                else:
                    print("You only have", points, "points!!!")
            elif whichOne == 2:
                strPoints = int(input("How many points do you want to add to Strength? "))
                if strPoints <= points:
                    strength += strPoints
                    points = points - strPoints
                    print("You now have", strength, 'strength points!')
                else:
                    print("You only have", points, 'points!!!')
            elif whichOne == 3:
                heaPoints = int(input("How many points do you want to add to Strength? "))
                if heaPoints <= points:
                    health += heaPoints
                    points = points - heaPoints 
                    print("You now have", health, 'health points!')
                else:
                    print("You only have", points, 'points!!!')
            elif whichOne == 4:
                wisPoints = int(input("How many points do you want to add to Strength? "))
                if wisPoints <= points:
                    wisdom += wisPoints
                    points = points - wisPoints
                    print("You now have", wisdom, 'wisdom points!')
                else:
                    print("You only have", points, 'points!!!')
            else:
                print(whichOne, "is not a valid choice!")

    elif choice == 2:
        while takeAway != 0:
            takeAway = int(input('''
    0 - Quit
    1 - Take away from Dexterity
    2 - Take away from Strength
    3 - Take away from Health
    4 - Take away from Wisdom
    '''))
            if takeAway == 0:
                print("Okay")
            elif takeAway == 1:
                dexTake = int(input("How many points do you want taken away? "))
                if dexTake <= dexterity:
                   dexterity = dexterity - dexTake
                   points += dexTake
                   print("You now have", dexterity, 'dexterity points!')
                else:
                    print("You only have", dexterity, "dexterity points to take!!!")
            elif takeAway == 2:
                strTake = int(input("How many points do you want taken away? "))
                if strTake <= strength:
                   strength = strength - strTake
                   points += strTake
                   print("You now have", strength, 'strength points!')
                else:
                    print("You only have", strength, "strength points to take!!!")
            elif takeAway == 3:
                heaTake = int(input("How many points do you want taken away? "))
                if heaTake <= health:
                   health = health - heaTake
                   points += heaTake
                   print("You now have", health, 'health points!')
                else:
                    print("You only have", health, "health points to take!!!")
            elif takeAway == 4:
                wisTake = int(input("How many points do you want taken away? "))
                if wisTake <= wisdom:
                   wisdom = wisdom - wisTake
                   points += wisTake
                   print("You now have", wisdom, 'wisdom points!')
                else:
                    print("You only have", wisdom, "wisdom points to take!!!")
            else:
                print(takeAway, 'is not a valid choice!!!')
    elif choice == 3:
        print('Dexterity:', dexterity)
        print('Strength:', strength)
        print('Health:', health)
        print('Wisdom:', wisdom)
        print("Points left:", points)
    elif choice == 0:
        print("Thank you!")
    else:
        print("That's not a valid choice.")

input = ("Press enter to exit.")
