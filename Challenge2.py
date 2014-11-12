#! /usr/bin/python3
# DD27.py
# Luke Gosnell
# 10/30/2014

# Design:
# Tell the user to add characters to their party and to give them points for the stats of their choice
# If the total of stats per character is more than 12, restart
# If any individual stat is less than 1 or greater than 4, restart
# When the user says that they don't want to add another player, print the a list that shows each character and their stats

party = []
person = ()
persons = 0
removedPoints=[]
removedpoints1=()

print("""
You have 30 points to spend on traits for each character

You can remove points if you wish
""")
print(" ")

strengthPoints = 0
healthPoints = 0
wisdomPoints = 0
dexterityPoints = 0

Player = "y"

for i in Player:
    while Player == "y":
        name = input("Name: ")
        strengthPoints = int(input("Strength: "))
        healthPoints = int(input("Health: "))
        wisdomPoints = int(input("Wisdom: "))
        dexterityPoints = int(input("Dexterity: "))
        stat = (strengthPoints + healthPoints + wisdomPoints + dexterityPoints)


        if stat > 30:
            print("You can't have a total of over 30 points. Try again.")
            exit()

        person = (name, strengthPoints, healthPoints, wisdomPoints, dexterityPoints)
        party.append(person)
        persons = persons + 1

        remove=input("Would you like to remove any points from any stat? (which stat?) ")
        if remove=='y':
            


        Continue = input("You have " + str(persons) + " in your party. Would you like to add another player? (y/n) ")
        if Continue == 'y':
            Player = 'y'
        else:
            Player = 'n'
print(party)




