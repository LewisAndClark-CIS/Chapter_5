# Chapter 5, Challenge 2
# Author: Alton Stillwell
# Date: 11/12/14(mm/dd/yy)
##########################
# Design
# Create a variable named 'pointPool' to store the available points,
#start at value 30
# print a menu and initiate a loop by asking which trait the user would like to
#put points into
# Until the user enters 'quit' at the menu the loop will not stop
# When finished, print a final point chart
################################################################################
# Variables
pointPool = 30
strength = 0
health = 0
wisdom = 0
dexterity = 0
addRem = ""
# initiate loop
print("---MENU---")
print("Points available:", pointPool)
print("1-Strength:", strength)
print("2-Health:", health)
print("3-Wisdom:", wisdom)
print("4-Dexterity:", dexterity)
print("0-Quit")
print()
code = int(input("Enter code num: "))
while code != 0:
    if code == 1:
        addRem = input("(add) or (rem) points? ")
        if addRem == "add":
            points = int(input("How many points would you like to add? "))
            check = pointPool - points
            if check < 0:
                print("Not enough points!")
            else:
                strength = strength + points
                pointPool = pointPool - points
        elif addRem == "rem":
            points = int(input("How many points would you like to remove? "))
            check = strength - points
            if check < 0:
                print("Too many points!")
            else:
                strength = strength - points
                pointPool = pointPool + points
        else:
            print("Invalid input!")
    elif code == 2:
        addRem = input("(add) or (rem) points? ")
        if addRem == "add":
            points = int(input("How many points would you like to add? "))
            check = pointPool - points
            if check < 0:
                print("Not enough points!")
            else:
                health = health + points
                pointPool = pointPool - points
        elif addRem == "rem":
            points = int(input("How many points would you like to remove? "))
            check = health - points
            if check < 0:
                print("Too many points!")
            else:
                health = health - points
                pointPool = pointPool + points
        else:
            print("Invalid input!")
    elif code == 3:
        addRem = input("(add) or (rem) points? ")
        if addRem == "add":
            points = int(input("How many points would you like to add? "))
            check = pointPool - points
            if check < 0:
                print("Not enough points!")
            else:
                wisdom = wisdom + points
                pointPool = pointPool - points
        elif addRem == "rem":
            points = int(input("How many points would you like to remove? "))
            check = wisdom - points
            if check < 0:
                print("Too many points!")
            else:
                wisdom = wisdom - points
                pointPool = pointPool + points
        else:
            print("Invalid input!")
    elif code == 4:
        addRem = input("(add) or (rem) points? ")
        if addRem == "add":
            points = int(input("How many points would you like to add? "))
            check = pointPool - points
            if check < 0:
                print("Not enough points!")
            else:
                dexterity = dexterity + points
                pointPool = pointPool - points
        elif addRem == "rem":
            points = int(input("How many points would you like to remove? "))
            check = dexterity - points
            if check < 0:
                print("Too many points!")
            else:
                dexterity = dexterity - points
                pointPool = pointPool + points
    else:
        print("Invalid input!")
    print()    
    print("---MENU---")
    print("Points available:", pointPool)
    print("1-Strength:", strength)
    print("2-Health:", health)
    print("3-Wisdom:", wisdom)
    print("4-Dexterity:", dexterity)
    print("0-Quit")
    print()
    code = int(input("Enter code num: "))
# final output
print("-------------")
print("Final Points:")
print("Points available:", pointPool)
print("Strength:", strength)
print("Health:", health)
print("Wisdom:", wisdom)
print("Dexterity:", dexterity)

