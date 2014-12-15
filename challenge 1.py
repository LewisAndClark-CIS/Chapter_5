# challenge 1.py
# Date: 11/10/2014
# Created by: Zach Golik

import random
WORDS = ['saw', 'house', 'junk', 'cake', 'pool', 'heat']
newWords =''
while WORDS:
    position = random.randrange(len(WORDS))
    newWords = newWords + WORDS[position] + ' '
    WORDS = WORDS [:position] + WORDS[(position + 1):]

print(newWords)
