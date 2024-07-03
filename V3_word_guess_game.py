# Making guess word game things to do :

# Import the game data dict (contains arrays as key value pairs of name and three hints). 

# Make a greet() function that asks user if they wanna play or not.

# Make a start() function that will start the game details about how the game will go below:

# Start function will pick a random word from a dict of words, get it's length and display an empty underscore equal to the size of the word eg:- (word: elephant , empty line: _ _ _ _ _ _ _ _).

# User will have 10 tries after 2,3 wrong guesses it will show another hint until it tries reach 0, if user guess is right start another function that will show the win or loose screen.

# Use booleans to impliment which hint to show eg:- if (hint_1 == True): show hint else keep it hidden make use of this for 3 hints.
# Note: After every 2-3 answers that are guessed wrong, set one boolean to true otherwise the hint will not show. 

# Make a gameover() function that will take a boolean as parameter if user wins set the parameter to True and send it to the gameover() function to display the winnig screen, else display the loose screen if the boolean is wromg.

#This text below has the text colors as variables without them the code will not work-
RESET = '\033[0m'      # Reset to default
BOLD = '\033[1m'       # Bold
UNDERLINE = '\033[4m'  # Underline

# Foreground colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
LIME = '\033[92m'
# -----------------------------------------------------------------------------------------------------------------------------


# Step 1:- Importing the database, importing random (for random words), importing os (to use 'cls').
import random
import os
# Do not have any data currently i will make dummy data.
Words = {
    'name':["pizza","burger","cake","juice","apple"],
    'hint_1':['Very famous italian dish 1','Very commonly eaten food 1','very sweet 1','very liquid 1','red in color 1'],
    'hint_2':['Very famous italian dish 2','Very commonly eaten food 2','very sweet 2','very liquid 2','red in color 2'],
    'hint_3':['Very famous italian dish 3','Very commonly eaten food 3','very sweet 3','very liquid 3','red in color 3']
}

#Defining the greet function Everything that shows when game starts is displayed here
def greet():
    
    input_check = True #Using this to check for correct input set it to True before using

    print(RED+"Guess"+YELLOW+" the"+ CYAN+" word"+ PURPLE+" game"+RESET)
    print("Enter 1 to start game.")
    print("Enter 2 to exit.")
    
    while True:
        try: #Prevents ValueError's 
            while input_check == True:
                player_inpt = int(input("> "))
                
                if player_inpt == 1 or player_inpt == 2:
                    #print("The code reached here #1") #for testing
                    input_check = False
                    if player_inpt == 1:
                        start()
                        
                    elif player_inpt == 2:
                        print("Exiting...")
                        
                    break
                
                else:
                    print("Please enter 1 or 2.")
                    continue
            break
        except ValueError:
            print("Please enter 1 or 2.")
        
#Defining the start function all the game code goes in here.
def start():
    os.system("cls")
    random_number = random.randint(0,4)
    word_chosen = Words['name'][random_number]  # Picks random word at a random index.
    word_chosen_len = len(word_chosen)          # Gets the length of the chosen word.
    
    hint_1 = False  # Boolean used to display hint one for the word. 
    hint_2 = False  # Boolean used to display hint two for the word.
    hint_3 = False  # Boolean used to display hint one for the word.
    
    underlined_str = ["_"] * word_chosen_len # This displays the empty underline string equal to the size of the word.
    formatted_underline_str = ' '.join(underlined_str)
    tries = 10      # This is the total number of tries player gets.
    next_hint = 10   # The number that will show next hint every 3rd wrong guess.
    
    while(tries > 0):       # Starts the loop.
        
        if(tries == 10):    # Sets the hint 1 to True so it shows in the begining of the game.
            hint_1 = True
        if(tries == 7):     # Sets the hint 2 to True so it shows after 3 attempts.
            hint_2 = True   
        if(tries == 4):     # Sets the hint 3 to True so it shows after 6 attempts.
            hint_3 = True 
            
        # The code below is displayed when game starts.      
        print(UNDERLINE+"GUESS THE WORD"+RESET)
        print("Length: "+CYAN+str(word_chosen_len)+RESET+"  Tries: "+LIME+str(tries)+RESET)
        print(formatted_underline_str)
        
        # Checks for which hints to show.
        if(hint_1 == True):
            print("Hint 1: "+str(Words['hint_1'][random_number]))
        if(hint_2 == True):
            print("Hint 2: "+str(Words['hint_2'][random_number]))
        if(hint_3 == True):
            print("Hint 3: "+str(Words['hint_3'][random_number]))
        
        # Managing player input and matching the answer below.
        player_input = input("> ")
        player_input = player_input.lower()
        
        
        if player_input == '': 
            os.system("cls")
            print(RED + "Answer cannot be empty"+RESET)     # Shows error if the input is empty (DOES NOT DEDUCT TRIES).
            
            
        elif (len(player_input) > word_chosen_len):     # Keep this here so it prevents some cheeky people from just entering
            os.system("cls")                            # "abcdefghijklmnopqrstuvwxyz" and seeing the full answer.
            print(RED+"The answer you enter cannot be longer than the word\nNo attempts has been deducted."+RESET)
           
            
        elif(player_input == word_chosen):       # If the answer is correct it will set (win_or_loose) to True
            win_or_loose = True                  # before sending it to the gameover() function.
            gameover(win_or_loose,word_chosen)
            break                              
    
    
        elif(player_input != word_chosen):      # If the answer is not True it will :- 
            tries -= 1      # 1. Deduct a try (attempt).
            next_hint -=1   # 2. Deduct a value from next hint.
            
# The code below is used to see which letters are present in the input And in answer. Then, it will change the empty
# underline (_ _ _ _ _) to that letter if it is present eg:- (Word: "pizza", input: "people", new underline_str: "P _ _ _ _" ).

            for i in player_input:      # Using for-loop to go through each letter of the input
                input_letter = i
                index = 0
                
                while (index < word_chosen_len):    # Using while loop to go through each letter of the answer (index).
                    if(input_letter == word_chosen[index]):     # If it matches, change the underlined str to the letter at 
                        underlined_str[index] = input_letter    # that index.
                        formatted_underline_str = ' '.join(underlined_str)
                        index += 1                              # index += 1, so it moves forward even if finds a match.
                        
                    else:
                        index += 1      # Incase it does not find match just move's the code forward.
                        
                        
# when player runs out of attemps send the bool to gameover() function to display "Player lost message":                
    if(tries == 0):
        win_or_loose = False
        gameover(win_or_loose, word_chosen)
    
# Defining the gameover function all the code after game ends (win or lose) goes here.
def gameover(win_or_loose, word_chosen): 
    
    if win_or_loose == True: # Plays the win side of the function if player won.
        os.system('cls')                            
        print(BOLD+"Congrats! You got it right!")
        print("The word was: ",word_chosen+".")
        print("What would you like to do now\n1. To play again.\n2. To exit.\n")
         
        while True:    # Using 2 while loops, this one is used if player enters some other number other than 1 or 2.   
            while True:     # Make sure they enter a number.
                try:
                    choice = int(input("> "))
                    break
            
                except ValueError:
                    print("Please enter 1 or 2")

            if (choice == 1):       # If user inputs 1, Restart the game.
                start()
                break
                
            elif (choice == 2):     # If user inputs 2, End the program.
                print("Exiting...")
                break
            
            else:                   # If user inputs something else, keep asking.
                print("Please enter 1 or 2")
                continue

       
    elif win_or_loose == False: # Plays the lost side of the function if player lost.
        print("Sorry! you lost.")
        print("The word was:",word_chosen+".")
        print("What would you like to do now\n1. To play again.\n2. To exit.\n")
        
        while True:    # Using 2 while loops, this one is used if player enters some other number other than 1 or 2.   
            while True:     # Make sure they enter a number.
                try:
                    choice = int(input("> "))
                    break
            
                except ValueError:
                    print("Please enter 1 or 2")

            if (choice == 1):       # If user inputs 1, Restart the game.
                start()
                break
                
            elif (choice == 2):     # If user inputs 2, End the program.
                print("Exiting...")
                break
            
            else:                   # If user inputs something else, keep asking.
                print("Please enter 1 or 2")
                continue

       
greet()