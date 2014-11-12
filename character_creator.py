# character_creator
# author: Bo Meers

points = 30
hp = 0
wis = 0
dex = 0

print(
"""
                 Welcome to the character creator program!
                You will have a pool of 30 points to spend.
        You can spend it on strength, health, wisdom, and dexterity.
""")

stre = int(input("Add to strength: "))
points = points - stre

if points > 0:
    hp = int(input("Add to health: "))
    points = points - hp

if points > 0:
    wis = int(input("Add to wisdom: "))
    points = points - wis
        
if points > 0:
    dex = int(input("Add to dexterity: "))
    
        
print("\n\tYou have")
print("\tStrenght: " + str(stre))
print("\tHealth: " + str(hp))
print("\tWisdom: " + str(wis))
print("\tDexterity: " + str(dex))
