
SonFather = {"Tyler":"Jose",
        "Jose":"Tom",
        "Tom":"Luke",}

choice = None
while choice != "0":

    print(
    """
    Who's Your Daddy?
    
    0 - Quit
    1 - Look Up a Son/Father pair
    2 - Add a Son/Father pair
    3 - Delete a Son/Father pair
    4 - Change a Son/Father pair
    """
    )
    
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # get a definition
    elif choice == "1":
        Son = input("What pair do you want me to show?: ")
        if Son in SonFather:
            Father = SonFather[Son]
            print("\n", Son, "is the son of", Father)
        else:
            print("\nSorry, I don't know", Father)

    # add a term-definition pair
    elif choice == "2":
        Son = input("What son do you want me to add?: ")
        if Son not in SonFather:
            Father = input("\nWho's the father?: ")
            SonFather[Son] = Father
            print("\n", Son, "has been added.")
        else:
            print("\nThat son already exists!")

    # delete a term-definition pair
    elif choice == "3":
        Son = input("What son do you want me to delete?: ")
        if Son in SonFather:
            del SonFather[Son]
            print("\nOkay, I deleted", Son)
        else:
            print("\nI can't do that!")

    # Change a pair
    elif choice == "4":
        Son=input("What existing son would you like to change?: ")
        if Son in SonFather:
            Father = input("Who is the father?: ")
            SonFather[Son]=Father
            print(Son+" has a new daddy!!!")
        else:
            print("That doesn't exist!")
            
    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
  
input("\n\nPress the enter key to exit.")
