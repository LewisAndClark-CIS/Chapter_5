#Chapter5-3.py
#Karl Pearson
#11/13/14

import pickle
choice=None

daddy={"Kenji Himura": "Kenshin Himura", "Connor Kenway": "Haytham Kenway", "Ezio Auditore": "Giovanni Auditore", "Luke Skywalker": "Anakin Skywalker", "Edward Elric": "Hoenhiem"}
while choice != "0":
    print("""
		Who's Your Daddy?
              ---------------------
 
		0 - Quit
		1 - Who's your daddy
		2 - Add a daddy
		3 - Replace a daddy
		4 - Delete a daddy
    """)
    choice = input("Choice?: ")
    print()
	
    if choice == "0":
            print("Farewell.")

    elif choice=="1":
        print("Here are the sons, let's find the dad. :")
        for key in daddy:
            print(key)
        dadName=input("What's the sons name?: ")
        dadCap=dadName.title()
        if dadCap in daddy:
            print("Who's your daddy "+dadCap+"? "+"--> "+daddy[dadCap]+".")
        else:
            print("I don't know that son..")

    elif choice=="2":
        addDad=input("Let's add a new pair. Who is the dad?: ")
        addSon=input("What is the name of "+addDad+"'s son?: ")
        daddy.update({addSon: addDad})
        print("You added "+addDad+" as the daddy of "+addSon+".")

    elif choice=="3":
        print("Here are all the son's who have replacable dad's:")
        if daddy:
            for key in daddy:
                print("Who's your daddy",key,"?")
                print(" ",daddy.get(key))
            repDad=input("Which son would you want the daddy to be replaced for?: ")
            if repDad in daddy:
                print("Currently "+repDad+"'s daddy is "+daddy[repDad]+".")
                newDad=input("Who is the new dad?: ")
                daddy[repDad]=newDad
                print(repDad+" 's new daddy is now "+newDad+".")
                
        else:
            ("You have no dads. Create some to replace one.")

    elif choice=="4":
        delDad=input("Which daddy do you want to delete?: ")
        if delDad in daddy:
            sure=input("Are you sure you want to delete this daddy? Y/N: ")
            if sure=="Y":
                del daddy[delDad]
                print("Daddy was deleted.")
            else:
                print("Daddy was not deleted")
        else:
            print("Error. That dad does not exist.")
