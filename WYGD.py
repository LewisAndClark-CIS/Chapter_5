# WYD
# author: Bo Meers

import random
import os
num = 1
father = ['Robert','James','John','William','Richard','Charles','Donald','George','Joseph','Edward']
grandFather = ['Kenneth','Bill','Bob','William','George','Papi']
while num != 0:
    print(
    """
MENU
-----------------------
0 - exit
1 - enter name
2 - add father
3 - delete father
4 - add grandfather
5 - delete grandfather
6 - list names
-----------------------""")
    choice = int(input("Your Choice: "))
    if choice == 0:
        num = 0
        
    elif choice == 1:
        name = input("\nWhat is your name? ")
        ranFath = random.choice(father)
        print("Your father is " + ranFath)
        
    elif choice == 2:
        print("\nFATHERS: " + str(father))
        add = input("Who would you like to add? ")
        father.append(add)
        
    elif choice == 3:
        print("\nFATHERS: " + str(father))
        remove = input("Who would you like to remove? ")
        father.remove(remove)
    
    elif choice == 4:
        print("\nGRANDFATHERS: " + str(grandFather))
        add = input("Who would you like to add? ")
        grandFather.append(add)

    elif choice == 5:
        print("\nGRANDFATHERS: " + str(grandFather))
        remove = input("Who would you like to remove? ")
        grandFather.remove(remove)

    elif choice == 6:
        print("\nGRANDFATHERS: " + str(grandFather))
        print("FATHERS: " + str(father))
