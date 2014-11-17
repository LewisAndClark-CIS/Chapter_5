# Challenge2.py
# Author: Sam Coon
# Date: 11/10/14

points = 30
skills = {"Strength": [],
          "Health": [],
          "Wisdom" :[],
          "Dexterity": []}
choice = ""
while choice != "0" and points > 0:
    print("You have",points,"points to spend.\n")
    print(skills)
    print(
    """
    0 - Exit
    1 - Spend points
    2 - Remove points
    """
    )

    choice = input("Choice: ")

    if choice == "0":
        print("Goodbye.")

    elif choice == "1":
        attribute = input("\nWhat skill do you want to put points in(Strength/Health/Wisdom/Dexterity)? ")
        if attribute in skills:
            amount = int(input("\nHow many points do you want in this skill? "))
            if amount < points:
                amount2 = amount
                skills[attribute] = amount2
                points -= amount
                
            else:
                print("\nThat is to much points you only have 30.")
        else:
            print("\nNot a valid input try again.")
            attribute = input("\nWhat skill do you want to put points in(Strength/Health/Wisdom/Dexterity)? ")
        
    elif choice == "2":
        attribute = input("\nWhat skill do you want to remove points from(Strength/Health/Wisdom/Dexterity)? ")
        if attribute in skills:
            amount = int(input("\nHow many points do you want to remove? "))
            if amount > skills[attribute]:
                print("\nThere are not that many points in that skill.")
            else:
                amount2 = amount
                skills[attribute] -= amount2
                points += amount2
