## Chapter 5 Challenge 3
"""
Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of his father.
(You can use celebrities, fictional characters, or even historical figures for fun.)
Allow the user to add, replace, and delete sonfather pairs.
"""

def menu():
    print(
        """
       MENU
  1 - Add pair
  2 - Replace a pair
  3 - Delete a pair
  4 - Look up a name
  """)

pairs ={}
listofkeys = pairs.keys()
lskeys = [listofkeys]
start = False
response = ""
decide = ""

while response not in ('yes','no'):
    response = input('Start program: ')

if response == 'yes':
    start = True

while start:
    menu()
    decide = input('Your choice: ')
    while decide not in ('1','2','3','4'):
        decide = input('Your VALID choice: ')
    if decide == '1':
        father = input("Enter father's name: ")
        son = input("Enter son's name: ")
        pairs[son] = father
        print(pairs)
    elif decide == '2':
        while pairs:
            for i in listofkeys:
                print('\n\t Father: '+ pairs[i] + ' | ' + 'Son: '+i)
            whatname = input('\nEnter the son of the pair you want to replace: ')
            newson = input('Enter new son name: ')
            newdad = input('Enter new father name: ')
            del pairs[whatname]
            pairs[newson] = newdad
            print(pairs)
            break
        if pairs == {}:
            print('\nYou need a pair in the databse first!')

    elif decide == '3':
        if pairs == {}:
            print('\nYou need a pair in the databse first!')
        while pairs:
            for i in listofkeys:
                print('\n\t Father: '+ pairs[i] + ' | ' + 'Son: '+i)
            whatname = input('\nEnter the son of the pair you want to delete: ')
            del pairs[whatname]
            break
    elif decide == '4':
        if pairs == {}:
            print('\nYou need a pair in the databse first!')
        while pairs:
            for i in listofkeys:
                print('\n\t Son: '+i)
            whatson = input('\nEnter a son to print its father: ')
            print('\n Father: '+pairs[whatson])
            break
