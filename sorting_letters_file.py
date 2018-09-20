#This program sorts the words present in a text document
#The file containing all the unsorted words is 'words.txt'
#'lines' is a list of all the words from the above file in a sorted manner 
#All the words are taken one by one and put into the file 'words1.txt'
#I used it to make different files for words starting with each letter as \
#searching a single file for a particular word to check whether the word is \
#meaning-ful or not was taking too much time with the configuration of my\
#laptop
#Also, this is probably the first time I actually applied any programming \
#language(let alone python) to solve real world problem


ft = open("words.txt", "r")
fr = open("words1.txt", "w")
lines = sorted(ft.readlines())
for item in lines:
    fr.write(item)
fr.close()
ft.close()


#By the way, a much more complex version for this program will be uploaded \
#soon to my github page ; that program will take a file containing words \
#starting with all the letters and make separate file for all the words \
#starting with a particular letter in a sorted order 
#Do check it out at https://github.com/SunnyVikasMalviya