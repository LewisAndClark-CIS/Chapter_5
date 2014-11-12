# WYD
# author: Bo Meers

import random
import os
num = 1
father = ['Robert','James','John','William','Richard','Charles','Donald','George','Joseph','Edward']
while num != 0:
    print(
    """
MENU
------------------
0 - exit
1 - enter name
2 - add father
3 - delete father
------------------""")
    choice = int(input("Your Choice: "))
    if choice == 0:
        num = 0
        
    elif choice == 1:
        name = input("What is your name? ")
        ranFath = random.choice(father)
        print("Your father is " + ranFath)
        
    elif choice == 2:
        print("FATHERS: " + str(father))
        add = input("Who would you like to add? ")
        father.append(add)
        
    elif choice == 3:
        print("FATHERS: " + str(father))
        remove = input("Who would you like to remove? ")
        father.remove(remove)
        
        
