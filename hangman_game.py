from subprocess import call
import pickle
import random
import time
import platform
import os
import player_details


USER = platform.system()
def clr_screen():
    if USER == 'Linux':
        call('clear')
    elif USER == 'Windows':
        r = os.system('cls')

hangman = {1:
    ["     ----------",
     "     |        |",
     "     |",
     "     |",
     "     |",
     "     |",
     "     |",
     "_____|_____"],
    2:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |",
         "     |",
         "     |",
         "     |",
         "_____|_____"],
    3:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |        |",
         "     |        |",
         "     |",
         "     |",
         "_____|_____"],
    4:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |       /|",
         "     |        |",
         "     | ",
         "     | ",
         "_____|_____"],
    5:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |       /|",
         "     |        |",
         "     |       / ",
         "     | ",
         "_____|_____"],
    6:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |       /|\ ",
         "     |        |",
         "     |       / ",
         "     | ",
         "_____|_____"],
    7:
        ["     ----------",
         "     |        |",
         "     |        O",
         "     |       /|\ ",
         "     |        |",
         "     |       / \ ",
         "     | ",
         "_____|_____",
         "\n\n\t\t\t\tGAME OVER!!!"],
}

with open('words.pickle', 'rb') as handle:
    all_words = pickle.load(handle)             #Stores all the words in the pickle file as a dictionary
chosen_list = list()                            #So that same word is not chosen again
chosen_letter_list = list()                     #Stores the used letters
wrong_choice = 0                                #Number of times player made the wrong choice
correct_choice = 0                              #Number of times player chose the correct letter
life = 7                                        #Player life(health) remaining
win = True

print('\n\n\t\t\t\t\t\t\tWELCOME TO HANGMAN')
print('INSTRUCTIONS')
print('You are basically just supposed to guess the word.')
print('You can either guess a single letter or the word itself.')
print("You can have a total of 7 wrong guesses for each word, after which you'll die.")
print('Your health will reset after each level.')
print('Your score will be the total number of words you gussed right.')

if not os.path.isfile('highscores.pickle'):
    player_details.reset_scores()

player_details.highscorePrint()                 # Print current high scores
print('\nPLAYER NAME')

name = player_details.player_info()             # Inputs for player info
print('\t\t\t\t\t\t\tGame will start shortly')
time.sleep(2)

def wordPrint(game_word, chosen_letter_list):   #To print the game word
    for letter in game_word:
        if letter in  chosen_letter_list:
            print(letter, end=" ")
        else:
            print("_", end=" ")

def hangmanPrint(wrong_choice):                 #To print the hangman
    if wrong_choice:
        hang = hangman[wrong_choice]
        for i in hang:
            print(i)

def gamewordChoice():
    rand_value = random.randint(1, 226)             #Choose a random word
    while rand_value in chosen_list:
        rand_value = random.randint(1, 226)
    
    chosen_list.append(rand_value)

    game_word = all_words[rand_value].upper()       #Choose the game word
    game_word_len = len(game_word)                  #Length of the word

    #print(game_word)                               #Debugging purpose
    #print(game_word_len)                           #Debugging purpose
    print("Health: ", "■ "*life)
    print(("\n\n"))
    for i in range(0, game_word_len):               #Printing the blank spaces according to the length of the word
        print("_", end=" ")
    return game_word


while wrong_choice < 7:                         #Game loop
    if win:
        clr_screen()
        win = False
        correct_choice = 0
        life = 7
        wrong_choice = 0
        chosen_letter_list.clear()
        print('\t\t\t\t\t\t\tLevel: ', (len(chosen_list) + 1))
        game_word = gamewordChoice()
    
    print('\n')
    user_choice = input("\nEnter your guess here: ").upper()
    
    if not user_choice.isalpha():
        continue

    if len(user_choice) > 1:                    #Guessing the whole word
        if user_choice == game_word:
            clr_screen()
            win = True
            print('\t\t\t\t\t\t\tLevel: ', len(chosen_list))
            print("Health: ", "■ "*life)
            print("Yaaayyy!!!\nYou found that word...")
            print("\n\n")
            hangmanPrint(wrong_choice)
            print("\n")
            print('Moving to the next level')
            time.sleep(2)
        else:
            clr_screen()
            wrong_choice += 1
            life = 7 - wrong_choice
            print('\t\t\t\t\t\t\tLevel: ', len(chosen_list))
            print("Health: ", "■ "*life)
            print("You guessed: ", user_choice)
            print("Whoops!\nWrong guess. Try again.")
            print("\n\n")
            wordPrint(game_word, chosen_letter_list)
            print("\n\n")
            hangmanPrint(wrong_choice)
            print("\n")
            
    elif user_choice in game_word:              #Guessing one letter
        clr_screen()
        print('\t\t\t\t\t\t\tLevel: ', len(chosen_list))
        if user_choice in chosen_letter_list:
            print("You've tried that letter before.")
        else:
            correct_choice += game_word.count(user_choice)
            chosen_letter_list.append(user_choice)
        print("Health: ", "■ "*life)
        print("You guessed: ", user_choice)
        print("\n\n")
        wordPrint(game_word, chosen_letter_list)
        print("\n\n")
        hangmanPrint(wrong_choice)
        print("\n")
                
    else:
        clr_screen()
        print('\t\t\t\t\t\t\tLevel: ', len(chosen_list))
        if user_choice in chosen_letter_list:
            print("You've tried that letter before.")
        else:
            chosen_letter_list.append(user_choice)
            wrong_choice += 1
        life = 7 - wrong_choice
        print("Health: ", "■ "*life)
        print("You guessed: ", user_choice)
        print("\n\n")
        wordPrint(game_word, chosen_letter_list)
        print("\n\n")
        hangmanPrint(wrong_choice)
        print("\n")
        
    if correct_choice == len(game_word):
        win = True
        print("Yaaayyy!!!\nYou found that word...")
        print('Moving to the next level')
        time.sleep(2)
    
    if wrong_choice == 7:
        print("The word was ", game_word)
        player_details.playerwrite(name, (len(chosen_list) - 1))
