# Challenge 4, chapter_5
# Author: Alton Stillwell
# Date: 11/19/14
#########################
# Variables/ Dictionary
pairs = {"Scooby Doo":["Brian","Snoopy"],"Luke":["Vader","George Lucas"]}
# Initiating loop
print()
print("""---MENU---
0-----Quit
1----Query
2------Add
3--Replace
4---Delete
""")
choice = int(input("Enter option number: "))
while choice != 0:
    if choice == 1:
        son = input("\nWhich name would you like to query? ")
        if son in pairs:
            print(son+"'s father is",pairs[son][0])
            print(son+"'s grandfather is",pairs[son][1])
        else:
            print("Name not found")
    elif choice == 2:
        son = input("\nEnter son's name: ")
        if son not in pairs:
            father = input("Enter father's name: ")
            grandFather = input("Enter grandfather's name: ")
            pairs[son] = ["",""]
            pairs[son][0]=father
            pairs[son][1]=grandFather
            print(son,"has been added")
        else:
            print("That term already exists! Try redefining it.")
    elif choice == 3:
        son = input("\nWhat father-son pair do you want to redefine(enter name of son)? ")
        if son in pairs:
            father = input("What is the new father? ")
            pairs[son][0] = father
            grandFather = input("What is the new father? ")
            pairs[son][1] = grandFather
            print(son,"has been redefined")
        else:
            print("That name doesn't exist! Try adding it.")
    elif choice == 4:
        son = input("\nWhat father-son pair do you want to delete? ")
        if son in pairs:
            del pairs[son]
            print("Successfully deleted",son)
        else:
            print(son,"not found!")
    else:
        print("\nInvalid choice!")
    print()
    print("""---MENU---
0-----Quit
1----Query
2------Add
3--Replace
4---Delete
""")
    choice = int(input("Enter option number: "))
# Final output
print()
input("Press <enter> to close")
