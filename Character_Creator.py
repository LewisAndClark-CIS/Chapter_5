CustomizablePoints=30
GoodMod=False
UsedPoints=0
print("Welcome to Character Creator.")
print("You will tell me what you want for your strength, wisdom, health, and dexterity.")
while GoodMod==False:
    while UsedPoints != 30:
        Strength=int(input("How many points do you want for Strength? "))
        PointsLeft=30-Strength
        print("You have "+str(PointsLeft)+" points left.")
        Health=int(input("How many points do you want for Health? "))
        PointsLeft=PointsLeft-Health
        print("You have "+str(PointsLeft)+" points left.")
        Wisdom=int(input("How many points do you want for Wisdom? "))
        PointsLeft=PointsLeft-Wisdom
        print("You have "+str(PointsLeft)+" points left.")
        Dexterity=int(input("How many points do you want for Dexterity? "))
        UsedPoints=Strength+Health+Wisdom+Dexterity
    print("Your Character's status:")
    print("Strength: "+str(Strength))
    print("Health: "+str(Health))
    print("Wisdom: "+str(Wisdom))
    print("Dexterity: "+str(Dexterity))
    Finished=input("Is this chracter cusmoization okay with you? ")
    while Finished not in ["y","Y","yes","no","n","N"]:
        print("That is not a option.")
        Finished=input("Is this character customization okay with you? ")
    if Finished in ["no","n","N"]:
        print("I am sorry about this but you will need to restart this process.")
        UsedPoints=0
    else:
        print("Thank you for your time.")
        GoodMod=True
        
    
    
                 
