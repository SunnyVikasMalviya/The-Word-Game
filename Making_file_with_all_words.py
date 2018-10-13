# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 21:53:32 2018

@author: Sunny
"""
'''So I have files named a.txt, b.txt, ... and all these file contains words \
starting from the respective file name letters. I wanted to make a single file\
of words to use for my word game and so i created this little program.'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

#counter to count the number of words in the final file
cnt = 0

#A new file to save all the words found in the files
new_file = open("..\\Words.txt", "w")
#Open each file containing words starting with the file name letter 
for ch in letters :
    #One by one opening each file
    file = open(str("..\\Letters\\"+ch+".txt"), "r")
    #Location of the folder containing letters files
    #Taking all the words in the file in a list
    words = file.readlines()
    #Sorting the list
    words.sort()
    #Writing each word in the file and counting the number of words written
    for each_word in words  :
        new_file.write(each_word)
        cnt += 1;
    file.close()
#print("Done!!!",cnt)         #For Debugging

new_file.close()