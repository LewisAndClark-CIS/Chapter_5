#Chapter 5 Challenges #2

points = 30
editskill = True
count = 0
whatSkill = ""
howmuch = 0
subOrAdd = ""
ValidAdd = False
ValidSub = False
AttribDB = {"Strength": ['0'],
            "Health": ['0'],
            "Wisdom": ['0'],
            "Dexterity": ['0'],
            }
listofkeys = AttribDB.keys()

yes = ('y','yes','yeah','yup')
no = ('n','no','nope')

def Add():
    global points, whatSkill, AttribDB, listofkeys, ValidAdd
    while ValidAdd == False:
        while True:
            try:
                print('Enter 0 to edit another skill')
                print('\nYou have ' + str(points) + ' points and there are '+ AttribDB[whatSkill][0] + ' points in ' + whatSkill)
                howmuch = int(input('Enter how many points you would like to add to ' + whatSkill + ': '))
                break
            except ValueError:
                print('Enter only numbers!')
        points -= howmuch
        numToAdd = int(AttribDB[whatSkill][0])+ int(howmuch)
        if (points >= 0 and howmuch > 0):
            break
        if points < 0:
            print('\nYou can not go below 0 points!')
        if numToAdd < 0:
            print("\nYou can't add negative numbers! ")
        points += howmuch

    if AttribDB[whatSkill]:
        del AttribDB[whatSkill][::]
    AttribDB[whatSkill] += [str(numToAdd)]
    print()
    print('You have '+str(points)+ ' points left.')
    for i in listofkeys:
        print('\t-' + i)
        templist = AttribDB[i]
        for j in templist:
            print('\t\t- ' + j + ' points')



def Sub():
    global points, whatSkill,AttribDB, listofkeys
    ValidSub = False
    while ValidSub == False:
        while True:
            try:
                print('\nEnter 0 to edit another skill')
                print('You have ' + str(points) + ' points and there are '+ AttribDB[whatSkill][0] + ' points in ' + whatSkill)
                howmuch = int(input('Enter how many points you would like to subtract from ' + whatSkill + ': '))
                if (howmuch > -1):
                    break
                else:
                    print('Not a valid input.')
            except ValueError:
                print('Enter only numbers!')
        points += howmuch
        numToSub = int(AttribDB[whatSkill][:]) - howmuch
        if ((points < 30) and (numToSub > 0)) or (howmuch == 0):
            break
        if points < 0:
            print('\nYou can not go below 0 points!')
        if numToSub < 0:
            print("\nYou can't Subtract more than whats in the skill!")
        points -= howmuch
    if AttribDB[whatSkill]:
        del AttribDB[whatSkill][::]
    AttribDB[whatSkill] += str(numToSub)
    print()
    print('You have '+str(points)+ ' points left.')
    for i in listofkeys:
        print('\t-' + i)
        templist = AttribDB[i]
        for j in templist:
            print('\t\t- ' + j + ' points')



while editskill:
    confirm = input('Edit skill? ')
    confirm = confirm.lower()
    if confirm in no:
        editskill = False
    while whatSkill not in listofkeys:
        for i in listofkeys:
            print('\t-' + i)
            templist = AttribDB[i]
            for j in templist:
                print('\t\t- ' + j + ' points')
        whatSkill = input('Edit what skill: ')
        whatSkill = whatSkill.title()
    while subOrAdd.lower not in ('a','s'):
        print('\nPress <enter> to go back and edit another skill.')
        subOrAdd = input('(A)dd or (S)ubtract from ' + whatSkill + ': ')
        if subOrAdd == "":
            whatSkill = ""
            while whatSkill not in listofkeys:
                print()
                print('You have '+str(points)+ ' points left.')
                for i in listofkeys:
                    print('\t-' + i)
                    templist = AttribDB[i]
                    for j in templist:
                        print('\t\t- ' + j + ' points')
                whatSkill = input('Edit what skill: ')
                whatSkill = whatSkill.title()
        if subOrAdd.lower() == 'a':
            Add()
            subOrAdd = 'A value'
        if subOrAdd.lower() == 's':
            Sub()
            subOrAdd = 'A value'
        
    while whatSkill not in listofkeys:
        whatSkill = input('Edit what skill: ')
    if points == 0:
        exitres = input('Are you finished putting points in? ')
        if exitres in yes:
            editskill = False

for i in listofkeys:
    print('\t-' + i)
    templist = AttribDB[i]
    for j in templist:
        print('\t\t- ' + j + ' points')

print()
input('Press <enter> to exit.')
