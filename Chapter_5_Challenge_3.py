# Name: Chapter 5 Challenge 3
# Author: Brianna Melius

import random
choice = None
families = {
    "Family":[]
    }
dad=["David Tennant", "Morgan Freeman","Matt Smith"]
print(
"""
Who's Your Daddy?

0 - Quit
1 - Add a new son to inventory
2 - Add new father to inventory
3 - Delete a son in inventory
4 - Delete a father in inventory 

"""
)
while choice != 0:
    
    choice = int(input("Enter a code number: "))
    if choice == 1:
        yes=True
        while yes != False:
            son=input("What is the sons name: ")
            fath=random.choice(dad)
            fam=[fath,son]
            print(fam)
            families["Family"]=fam
            again = input("Do you want to go again: ")
            if again=="yes":
                yes=True
            elif again=="no":
                yes=False
    elif choice == 2:
        yes=True
        while yes != False:
            fath=input("What is the father's name?: ")
            son=random.choice(son)
            fam=(fath,son)
            print(fam)
    elif choice == 3:
        yes=True
        while yes != False:
            print(families)
            son=input("Which son would you like to delete?: ")
            families["Family"].remove(son)
            again = input("Do you want to go again: ")
            if again=="yes":
                yes=True
            elif again=="no":
                yes=False
            
            
        
