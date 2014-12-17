SonFather = {"Goku":("Father", "Bardock"),"Bardock":("Father", "Tom Morrissey"),
             "Tom Morrissey":("Father", "Luke Goesnell"),"Luke Goesnell":("Father", "Tyler Guerra"), "Tyler Guerra":("Father", "Jose Chica"), "Jose Chica":("Father","Goku")}
choice = None
while choice != "0":

    print(
    """
    Who's your Daddy?
    
    0 - Quit
    1 - Look Up a Son to know who the father is
    2 - Add a Son-Father pair
    3 - Change a Son-Father pair
    4 - Delete a son-Father pair
    5 - Look Up The Extended Family
    """
    )
    
    choice = input("Choice: ")
    print()

    
    if choice == "0":
        print("Good-bye.")

    
    elif choice == "1":
        Son = input("What Son do you want me to find")
        if Son in SonFather:
            Father = SonFather[Son]
            print("\n", Son+"'s dad is", Father)
        else:
            print("\nSorry bruh, I don't know "+Son+"'s father.")

    
    elif choice == "2":
        Son = input("Who do you want me to add?: ")
        if Son not in SonFather:
            Father = input("\nWho's "+Son+"'s daddy? ")
            SonFather[Son] = Father
            print("\n"+Son+" and "+Father+" has been added.")
        else:
            print("\nThat Son already has a dad!  Try changin it.")

    
    elif choice == "3":
        Son = input("What Son Do you want to have a different father for? ")
        if Son in SonFather:
            Father = input("Who is "+Son+"'s daddy? ")
            SonFather[Son]=Father
            print("\n"+Son+" has been a new daddy.")
        else:
            print("\nThat Son doesn't exist!  Try adding that person.")
       
    
    elif choice == "4":
        Son = input("What Son do you want me to delete?: ")
        if Son in SonFather:
            del SonFather[Son]
            print("\nOkay, I deleted", Son)
        else:
            print("\nI can't do that!", Son, "doesn't exist in the dictionary.")

    elif choice == "5":
        ExtendedFamily=0
        Continue= "y"
        Son=input("Who would you like to look up?")
        while ExtendedFamily != 7 and Continue in ["y", "Y", "yes", "Yes"]:
            if Son in SonFather:
                Father=SonFather[Son]
                print(Son+"'"+"s father is ", Father[1], ".")
                ExtendedFamily += 1
                if ExtendedFamily<7:
                    string="Do you wish to find out who is "+Father[1]+"'"+"s dad? "
                    Continue=input(string)
                    while Continue not in ["y","Y","yes","Yes","n","N","No","no","NO"]:
                        string = "Do you wish to find out who is "+Father[1]+"'"+"s dad? "
                        Continue=input(string)
                Father=Father[1]
                Son=Father
               
    else:
        print("\n",choice, "isn't a valid choice.")
  
input("\n\nPress the enter key to exit.")
