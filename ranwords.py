# Words
# author: Bo Meers

import random
words = ['come','go','bye','chips','drinks','worms','computers','mouse','house','chairs','dolls','shoes','books','food']
usedWords = []
total = 13

while total != -1:
    ran = random.randint(0,total)
    print(words[ran])
    words.remove(words[ran])
    total -= 1
    
