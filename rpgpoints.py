points = int(30)
attributes = {'strength': 0, 'health': 0, 'wisdom':0, 'dexterity': 0}
functions = ['add points', 'take points', 'see points', 'exit']

def adding_points():
    global points
    print("You have",  points, "points left")
    choice = input("What attribute to distribute to? Strength? Health? Wisdom? Dexterity?")
    print("\n")
    if choice in attributes:
          add = int(input("\nHow many points?"))
          if add <= points:
              attributes[choice] += add
              points -= add
              print(choice, ': ', (attributes[choice]))
          else:
              print("Invalid input of points.")

def sub_points():
    choice = input("Which attribute to distribute to? Strength? Health? Wisdom? Dexterity?")
    if choice in attributes:
        sub = int(input("How many points? "))
        if sub >= attributes[choice]:
            attributes[choice] -= sub
            points += sub
            print(choice, ': ', (attributes[choice]))
        else:
            print("Invalid input of points.")

def see_points():
    for x in attributes:
        print(x, ': ', (attributes[x]))

name = input("What's your character's name?")
print("Hi,", name)
while True:
    print("Would you like to add points, take points, see points in each attribute or exit?")
    for x in functions:
        print(x, ': ', 'press', (functions.index(x) + 1))
    print("\n")
    func = int(input())
    if func == 1:
              adding_points()
    if func == 2:
              sub_points()
    if func == 3:
              see_points()
    if func == 4:
              break
print("Congratulations! You created your own character! Great Job!")


                  
        
    
        
    
