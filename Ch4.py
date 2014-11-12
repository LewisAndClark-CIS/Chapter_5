#Challenge 3
#Chris Looney
#11/11/14
dic = {'Christopher': ['Chris', 'William']}
choice = None
while choice != '0':
    print(((
        """
-------------------------
 1 - Check Father
 2 - Add Son and Father
 3 - Change Father of Son
 4 - Delete Father and Son Pair
 5 - Check for Grandfather
 0 - Exit
-------------------------
       """
        )))
    choice = input('Enter an option: ')
    if choice == '1':
        nameCheck = input('Whos daddy you lookin for? ')
        if nameCheck in dic:
            print(dic[nameCheck])
        else:
            print('Name not found. Try adding it!')
    elif choice == '2':
        sonAdd = input('Whats the name of the son? ')
        dadAdd = input('Whats the name of the father? ')
        dic[sonAdd] = [dadAdd]
        print('Done!')
    elif choice == '3':
        nameCheck = input('Whose dad are you trying to change? ')
        if nameCheck in dic:
            newDad = input('Who will the new dad be? ')
            dic[nameCheck] = [newDad]
            print('Done!')
        else:
            print('They don\'t even exist...')
    elif choice == '4':
        nameDel = input('Who do you wanna delete? ')
        if nameDel in dic:
            del dic[nameDel]
            print('Done!')
        else:
            print('They aren\'t even here...')
            
    elif choice == '5':
        gpaCheck = input('Whose grandpa you lookin for? ')
        if gpaCheck in dic:
            print(dic[gpaCheck])
        else:
            print('They don\'t exist')
