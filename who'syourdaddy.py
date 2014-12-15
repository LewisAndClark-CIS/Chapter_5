pairs = {"Johnny Depp": "John Christopher Depp",
         "Arnold Schwarzenegger": "Gustav Schwarzenegger",
         "Dwayne Johnson": "Rocky Johnson",
         "Michael Jackson": "Joe Jackson",
         "Elvis Presley": "Vernon Presley",
         "Harry Potter": "James Ptter"}

choice = None
while choice != "0":

    print
    (
    """
    Who is YOUR Daddy?


    The very first Father-Son Look-up Game Show

    0 - Quit
    1 - Look Up a Pair
    2 - Add a Pair
    3 - Change the Father
    4 - Delete a Pair
    5 - Replace an entire Pair
    """
    )

    
    choice = input("Enter a choice from above: ")

    if choice == 0:
        print("Decided to Quit.")
    elif choice == "1":
        print("This is your current list nn", pairs)
    elif choice == "2":
        pair = input("Who's the son? ")
        if pair not in pairs:
            father = input("Who's the daddy? ")
            pairs[pair] = father
            print("n", pair, "has been added.")
        else:
            print("That term already exists! Try redifining it instead.")
    elif choice == "3":
        pair = input("Name the son of the father to get rid of: ")
        if pair in pairs:
            father = input("Who's the new father?: ")
            pairs[pair] = father
            print("n", pair, "has been added.")
        else:
            print("That term dosen't exist! Why not add it?")
    elif choice == "4":
        pair = input("What pair do you want to delete?: ")
        if pair in pairs:
            del pairs[pair]
            print("Okay,", pair, "has been deleted.")
    elif choice == "5":
        pair = input("What pair do you want to replace?: ")
        if pair in pairs:
            del pairs[pair]
            print("Okay, I deleted", pair)

            pair = input("Who's the new son?: ")
            if pair not in pairs:
                father = input("Who's the new father?: ")
                pairs[pair] = father
                print("n", pair, "has been added.")

        else:
            print("Sorry, but", pair, "dosen't exist in the dictionary.")
            
            

            
        
    
        
