# Challenge1.py
# Author: Sam Coon
# Date: 11/10/14

import random

WORDS = ["Apple","Cane","Bus","Clone"]

choice1 = random.choice(WORDS)
WORDS.remove(choice1)

choice2 = random.choice(WORDS)
WORDS.remove(choice2)

choice3 = random.choice(WORDS)
WORDS.remove(choice3)

choice4 = random.choice(WORDS)
WORDS.remove(choice4)

choices = (choice1,choice2,choice3,choice4)
print(choices)
