#Chapter 5 - Challenge 1
#Chris Looney
#November 10,2014

import random

first_word = input("Please enter your first word: ")
second_word = input("Please enter your second word: ")
third_word = input("Please enter your third word: ")
fourth_word = input("Please enter your fourth word: ")
fifth_word = input("Please enter your fifth word: ")

word_list = (first_word,second_word,third_word,fourth_word,fifth_word)
random_word_list = []
while len(random_word_list) != len(word_list):
    word = random.choice(word_list)
    if word not in random_word_list:
        random_word_list += word

print(random_word_list)

input("\n\nPress enter to exit...")
