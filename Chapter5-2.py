#Challenge5-2.py
#By: Karlos Calvillo
#11/11/14

party=[]
person=()
strength=0
health=0
wisdom=0
dexterity=0
add=input('Would you like to add a party member? Y/N: ')
while not add == "Y" and "N":
    print('You may only choose [Y]es or [N]o')
    add=input('Would you like to add a party member? Y/N: ')
while add == "Y":
    name=input('What is your name? ')
    characterStats=0
    print('Customize your stats')
    while characterStats!=30: 
        print('Choose a value for each stat(You may only have 30 points total)')
        strength=int(input('Strength stat: '))
        health=int(input('Health stat: '))
        wisdom=int(input('Wisdom stat: '))
        dexterity=int(input('Dexterity stat: '))
        characterStats=strength+health+wisdom+dexterity
        if characterStats>30:
            print('You have too many points, try again')
            strength=int(input('Strength stat: '))
            health=int(input('Health stat: '))
            wisdom=int(input('Wisdom stat: '))
            dexterity=int(input('Dexterity stat: '))
        elif characterStats<30:
            print("You don't have enough points, try again")
            strength=int(input('Strength stat: '))
            health=int(input('Health stat: '))
            wisdom=int(input('Wisdom stat: '))
            dexterity=int(input('Dexterity stat: '))
            print(str(characterStats))
        elif characterStats==30:
            print('You have completed character setup')
            print('Your stats are: ')
            print('Strength: '+str(strength))
            print('Health: '+str(health))
            print('Wisdom: '+str(wisdom))
            print('Dexterity: '+str(dexterity))
        sure=input("Are you sure you want these stats?: Y/N ")
        if sure=="Y":
            person=(name+','+str(strength)+','+str(health)+','+str(wisdom)+','+str(dexterity))
            party.append(person)
            print(party)
            add=input('Would you like to add a party member? Y/N: ')
        elif sure=="N":
            characterStats=0
            print("Reassign points")
if add=="N":
    print(party)
            
   
