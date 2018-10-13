# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:28:07 2018

@author: Sunny
"""
import random

consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',\
                  'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

def display_random_letters() :
    random_letter_produced = []
    num_vowels = random.randint(1,5)
    #print(num_vowels)
    #This first loop generates 5 to 9 random consonents
    while len(random_letter_produced) < (10 - num_vowels)  :
        random_letter = random.choice(consonents)
        if random_letter not in random_letter_produced :
            random_letter_produced.append(random_letter)
    #This second loop generates 5 to 1 random vowels that are left
    while len(random_letter_produced) < 10 :
        random_letter = random.choice(vowels)
        if random_letter not in random_letter_produced :
            random_letter_produced.append(random_letter)
            #remove the pound to print the letters in random order as they get
            #produced. They will be printed in separate lines
            #print (random_letter)  
    #This will display the list of random letters in alphabetical order in 
    #a single line as a list
    print (sorted(random_letter_produced))   
    return random_letter_produced