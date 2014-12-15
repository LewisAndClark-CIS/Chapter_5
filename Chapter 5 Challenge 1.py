# Name: Chapter 5: Challenge 1
# Date: November 12, 2014
# Author: Brianna Melius

# Design: create a program that prints a list of words in a random order; print all words, repeat none.
from random import shuffle

winterClothing = ["Hat","Glasses","Scarf","Coat","Gloves","Pants","Boots"]
shuffle(winterClothing)
print(winterClothing)
