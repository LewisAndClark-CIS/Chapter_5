# Name: Chapter 5: Challenge 2
# Date: November 12, 2014
# Author: Brianna Melius

# Design: 30 pts for 4 attr: Strength, Health, Wisdom, + Dexterity.
# should be able to assign and remove points from attr.

attributes = {'Strength:', 'Health:', 'Wisdom:', 'Dexterity:'}

print(
"""
Character Creator

Starting Points: 30
Attributes: Strength, Health, Wisdom, Dexterity.

0 - Quit
1 - Add more points to an attribute
2 - Take away points from an attribute


"""
)

choice = int(input("Please enter a number: "))
if choice == 0:
    input("Press 'Enter' to exit.")
elif choice == 1:
    attribute = input("Which attribute would you like to add points to? ")
    if attribute in attributes:
        points = int(input("How many points would you like to add?: "))
        attributes[attribute] = points
    else:
        print("That attribute does not exist.")

elif choice == 2:
    attribute = input("Which attribute would you like to take away points from? ")
    if attribute in attributes:
        points = int(input("How many points would you like to take away?: "))
        attributes[attribute] = points
    else:
        print("That attribute does not exist.")

