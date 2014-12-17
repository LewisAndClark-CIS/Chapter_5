CP=30
GoodMod=False
Used=0
print("Welcome lads to the Character Creator.")
print("You will tell me what you want for your STRength, WISdom, HEAlth, and DEXterity.")
while GoodMod==False:
    while Used != 30:
        STR=int(input("How many points do you want for Strength? "))
        PL=30-STR
        print("You have "+str(PL)+" points left.")
        HEA=int(input("How many points do you want for Health? "))
        PL=PL-HEA
        print("You have "+str(PL)+" points left.")
        WIS=int(input("How many points do you want for Wisdom? "))
        PL=PL-WIS
        print("You have "+str(PL)+" points left.")
        DEX=int(input("How many points do you want for Dexterity? "))
        Used=STR+HEA+WIS+DEX
    print("Character status:")
    print("STRength: "+str(STR))
    print("HEAlth: "+str(HEA))
    print("WISdom: "+str(WIS))
    print("DEXterity: "+str(DEX))
    GoodMod=True
done=input("Do you like your character? ")
while done not in ["y","Y","yes","no","n","N"]:
    print("INVALID OPTION!")
    done=input("Do you like your character? ")
if done in ["no","n","N"]:
    print("Sorry mate looks like you have to start over.")
    Used=0
else:
    print("Thank you for your time.")
    GoodMod=True
