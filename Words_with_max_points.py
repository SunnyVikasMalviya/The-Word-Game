# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 23:11:53 2018

@author: Sunny
"""

from Random_Letters_Producer import display_random_letters

#Score of each letter
score = {"a": 5, "c": 25, "b": 44, "e": 2, "d": 16, "g": 40, "f": 30, "i": 5,\
    		 "h": 8, "k": 64, "j": 90, "m": 25, "l": 17, "o": 5, "n": 5, "q": 80, \
    		 "p": 40, "s": 5, "r": 12, "u": 20, "t": 4, "w": 34, "v": 62, "y": 34,\
    		 "x": 90, "z": 120, "\n": 0}

#Function to calculate the score of each word passed as a parameter
def scoring(word):
    total = 0
    for ch in word:
        total += score[ch]
    #The escape sequence \033[36m is used for coloring text into darkcyan
    #print(" Points Earned : \033[36m",total,"\033[0m")
    return total

#display_random_letters produces ten random letters in alphabetical order
letters = display_random_letters()
letters.append('\n')

#Dictionary to store words whose each letter belongs to the random letters list
words_with_random_letters = {}

#List to store words with the maximum points
max_points_words = [] 
file = open("..\\Words.txt", "r")
words_in_file = file.readlines()
for each_word in words_in_file :
    #Checking whether each letter in the word from the file is present in the \
    #random letter list and if so the score of the word is calculated and\
    #the word is added to the dictionary with its score
    for each_letter in each_word :
        if each_letter not in letters :
            break
    else :
        words_with_random_letters[each_word] = scoring(each_word)

#print(words_with_random_letters.items())          #For Debugging
print(max(words_with_random_letters.values()))

#To find words whose total equals the maximum points and storing them in a list
for each_item in words_with_random_letters :
    if words_with_random_letters[each_item] == max(words_with_random_letters.values()) :
        max_points_words.append(each_item)
       
print(max_points_words)