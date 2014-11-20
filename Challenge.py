# Chapter 5, Challenge 1
# Author: Alton Stillwell
# Date: 11/12/14(mm/dd/yy)
##########################
# Design
# create a list named 'words' to store mult. words
# create a loop to put all the words in a variable 'newWords'
# in a random order, not repeating the word
# Print 'newWords'
##########################
import random
# List
WORDS = ["The","Man","Sat","On","Sky","Apple","Wart","Car","Medicine"]
newWords = ""
# Loop
while WORDS:
    word = random.randrange(len(WORDS))
    newWords = newWords + WORDS[word] + " "
    WORDS = WORDS[:word]+ WORDS[(word+1):]
# Final Output
print (newWords)
