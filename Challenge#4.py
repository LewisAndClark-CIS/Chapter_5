import random
WORDS=["Batman","Superman","Green Latern","Green Arrow","Wonder Woman","Super Girl","Black Canary","Starfire","Zatanna"]
UsedWords=[]
while len(WORDS)>0:
    WordIndex=random.randrange(len(WORDS))
    Word=WORDS[WordIndex]
    print(Word)
    UsedWords.append(Word)
    WORDS=WORDS[:WordIndex]+WORDS[(WordIndex+1):]
