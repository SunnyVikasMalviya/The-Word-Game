# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:33:05 2018

@author: Sunny
"""
"""So I made a mistake while creating the files with all the words 
starting with the same letter. Rather than nameing them as a.txt, b.txt,...
 I mistakeingly named them as a (1).txt, a (2).txt,... 
 So I was made to create this program by destiny.
 By the way, do you remember when you started learning programming and 
 people used to say that you can solve real life problems with programming,
 I just started doing that and I think this is my second program that solves
 a real life problem. Just so you know, I have been doing programming since 
 last 4 years and have just solved the bookish questions till now. """

#A list of letters
#So we can loop through it and name our files
#could have done that with ASCII, but I found this method a lot more easier
# and intuitive
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i = 1

#We create a file named a.txt, b.txt, ... in subsequent iterations
#We copy all the words in the file a (1).txt, a (2).txt, ... in subsequent 
#iterations and make a list of the words
#Then simply loop through the list and write the words in the created files

for ch in letters:
    orig_file_name = "Letters\\a (" + str(i) +").txt"
    new_file_name = ch + ".txt"
    #print (orig_file_name)
    ori = open(orig_file_name, 'r')
    new = open(new_file_name, 'w')
    lines = ori.readlines()
    for line in lines:
        new.write(line)
    i = i+1
    ori.close()
    new.close()
print("Done!")


"""Although I thought it would take python a lot of time to copy all that 
content into new files; because it took python too long just to search a word
in just one file containin all the words, which again is why I started making 
these programs in the first place; surprisingly it took around 3 seconds to 
copy all that content which really amazed me"""