# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:10:19 2018

@author: Sunny
"""

from Random_Letters_Producer import display_random_letters
#display_random_letters displays ten random letters in alphabetical order
#The letters produced will be stored in a list 'letters'
letters = display_random_letters()

#Since each word contains a newline character at its end
letters.append('\n')

#A dictionary to store words as keys and their size as values
words_with_random_letters = {}

#A list containing words with the max size found
max_size_words = [] 
file = open("..\\Words.txt", "r")

#List containing all the words in the file
words_in_file = file.readlines()
for each_word in words_in_file :
    #Checking if all the letters in a word from the file is present in the \
    #list of random letters. If so, the word and its size is added to the \
    #dictionary
    for each_letter in each_word :
        if each_letter not in letters :
            break
    else :
        words_with_random_letters[each_word] = len(each_word)

#print(words_with_random_letters.items())          #For Debugging
#Prnting the maximum size of words from all the word sizes
print(max(words_with_random_letters.values()))

#Finding words with maximum size and appending them to the list
for each_item in words_with_random_letters :
    if words_with_random_letters[each_item] == max(words_with_random_letters.values()) :
        max_size_words.append(each_item)
       
print(max_size_words)