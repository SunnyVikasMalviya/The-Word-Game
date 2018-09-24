    #Jumbled Words Game
if __name__ == '__main__':    
    #Simple rules 
    #Maximum 5 and minimum 2 players can play the game at a time
    #Players will be given 10 random letters in alphabetical order to make \
    #meaningfull words with them
    #Each player gets 2 minutes to make a word
    """Still have to work on the timer part"""
    #Words can be anything between 3 to 20 letters
    #Given letters can be used as many times as required by the player 
    #Points will be given by summing the scores of each letter

    import random
    
    #import os
    #clear = lambda : os.system('cls')
    #The above two lines are not working; wanted to clear the screen
    """Many Commented statements were used for debugging and are not \
    removed in order to ease future modifications"""
    
    
    #Dictionary listing the points of all the letters 
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, \
    		 "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, \
    		 "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,  \
    		 "x": 8, "z": 10}
    consonents = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',\
                  'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']
    players_score = {}
    		 
    #Function to calculate the score of a player for a word that just got entered
    def scoring(word):
        total = 0
        for ch in word:
            total += score[ch]
        #The escape sequence \033[36m is used for coloring text into darkcyan
        print("\033[36m",total,"\033[0m")
        return total
    
    
    #Function to display random letters
    def display_random_letters():
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
    
    
    #Funtion to take input and validate the word
    def validate_entered_word(random_letter_produced):
        #take input
        entered_word = input("Make a word from the given letters:")
        entered_word.lower()    
        #check the size
        if len(entered_word) not in range(3,21):
            print("Word should be between 3 to 20 letters long. Zero Points.")
            return ""
        #check the letters are present in the random_letter_produced list
        for ch in entered_word:
            if ch.upper() not in random_letter_produced:
                print("Only given letters can be used. Zero Points.")
                return ""
        #Extracting first letter of the entered word
        first_letter = ""
        for first_letter in entered_word:
            break
        first_letter.lower()
        file_name = "Letters\\" + first_letter + ".txt"
        #check whether word is meaning-ful or not
        ft = open(file_name, "r")
        #file_words contains all words in the first_letter file
        x=0
        """Most Important!!! : Strings Are Immutable...I learned it the hard way"""
        """So the problem with searching the word in a file is that the words in\
        the text file are arranged in alphabatical order and that too with a '\n'\
        character attached to it. Hence to compare the entered_word with the words\
        in the text files, we have to attach a '\n' character at the end of the\
        entered_word. But strings are immutable. So we cannot directly go \
        entered_word += '\n', which was what I was doing. I had a hard time \
        thinking about this(with Mayukh and Ashu; By the way, Huge Help), just to \
        realize this and hence I had to make a totally new variable 'ew' just to \
        compare the strings in the text file and the string that was entered. """
        ew = entered_word + ('\n')
        file_word=first_letter
        print(entered_word)
        while file_word!="": 
            #print(file_word, " %d " % (x)),
            x += 1
            file_word = str(ft.readline())
            #if file_word == entered_word :
            if file_word == ew :        
                print("Word found!")
                ft.close()
                return entered_word
        else :
            print("Word not found!")
            ft.close()
            return ""
        #print(file_words)
        #dict_word.lower()      #If the word list has words with capitalised \
        #letters
    """    if entered_word in file_words :
            print("Word found")
            return entered_word
        else :
            print("Word not found")
            return ""  """
    """for dict_word in file_words:
            if dict_word == entered_word:
                ft.close()
                print ("Word found")
                return entered_word
            elif dict_word == "zzzzz" : 
                ft.close()
                print("Word not meaning-ful.Zero points.")
                return ""
        else :
            print("Not a meaning-ful word.Zero points.")
            ft.close()
            return ""      """  
    
    #Function to display the score of each player and the winner
    def display_results(number_of_players):
        for x in range(0, number_of_players):
            print("Player ", x+1, ":", players_score[x])
        v = list(players_score.values())
        k = list(players_score.keys())
        winner =k[v.index(max(v))] 
        print("One last thing. In case of more than one players having the" \
              "highest score, only one lucky player gets to win.")
        print("And the winner is ...(Suspence)... Player %d" % (winner+1))
        out()
            
            
    #Function that displays the Intro Menu
    def intro():
        print ("\nHi Gamers! What would you like to do?")
        print ("1. Play")
        print ("2. Read Rules")
        print ("3. Exit")
        try:
            intro_choice = int(input("Choose 1, 2 or 3:"))
            if intro_choice == 1:
                play()
            elif intro_choice == 2:
                rules()
            elif intro_choice == 3:
                out()
            else :
                print("\nGarib hai kya? Jitna bola utna ker na. Choose either 1, 2 or 3")
                intro()
        except ValueError:
            print("\nEnter an Intergeral Value.")
            #clear()       #To Clear Screen but it is not working
            intro()
        except :
            print("Something went very wrong.")
        
    
    #Function to play the game
    def play():
        num_of_players = int(input("How many of you are going to play?(Max 5):"))
        #Checking whether the number of players is in the limit of 2 to 5 or not
        if num_of_players not in range(2,6):
            print("Khelna hai ya nahi khelna hai? Sahi input dal na.")
            play()
        #The next 2 lines makes the dictionary 'players_score' long enough to be \
        #able to hold scores of all the players
        for x in range(0, num_of_players):
            players_score[x] = 0  
        print("\nLets start then")
        for x in range(1, 4):
            print("\033[4mRound ",str(x),"\033[0m")
            for y in range(0, num_of_players):            
                print("Player %d to play" % (y+1))
                random_letter_produced = display_random_letters()
                #random_letter_produced.append('\\')
                #random_letter_produced.append('n')
                entered_word = validate_entered_word(random_letter_produced)
                players_score[y] += scoring(entered_word)
                print(players_score[y])
                #players_score
        display_results(num_of_players)
        
    
    #Function to display the rules
    def rules():
        #clear()
        #The escape sequence \033[4m Text is used to underline Text
        #The escape sequence \033[0m is used to represent where to end the \
        #previously used escape sequence... in this case underline
        print("\n\n\033[4mSimple rules\033[0m\n")
        print("Maximum 5 and minimum 2 players can play the game at a time")
        print("5 rounds will be played")
        print("Players will be given 10 random letters in alphabetical order", \
              "to make meaning-ful words with them")
        #print("Each player gets 2 minutes to make a word")
        print("Words can be anything between 3 to 20 letters")
        print("Given letters can be used as many times as required by the player")
        print("Points will be given by summing the scores of each letter")
        print("Zero points will be awarded for making words without meaning" \
              "with size outside the size limits\n")
        intro()
        
    
    #Function to come out of the game
    def out():
        print("Bye then! Go and have a life.")
    
    
    #scoring()
    #display_random_letters()
    #validate_entered_word()
    #display_results()
    intro()
    #play()
    #rules()
    #out()
