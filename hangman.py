#Hangman Project
#filename: hangman.py
#Name: JASMINE IRANI

import random
from words import word_list
    
def getRandom():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    #print('_'*len(word))
    word_completion = '_'* len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print("Let's play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Enter your guess:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list) 
                #1____
                if "_" not in word_completion:
                    guessed = True
            #print(word_completion)

        elif len(guess) == len(word)and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                #'test' != 'text'
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
        else:
            print('Guess not valid') 
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry you ran out of tries. the word was "+word, "maybe next time")
    

def display_hangman(tries):
    stages = [ #6 final stage: head, torso, both arms, both legs
            """
                 ------------
                    |     |
                    |     o
                    |    \\//
                    |     |
                    |    / \\
                    -
            """,
            #5 head, torso,both arms, and one leg
            """
                 ----------
                    |      |
                    |      o
                    |      |
                    |      /
                    -
            """,
            #4 head, torso, and both arms
            """
                 -------
                    |     |
                    |     o
                    |    \\//
                    |      |
                    |
                    -
            """,
            #3 head, torso, and one arm
            """   
                 --------
                    |      |
                    |      o
                    |     \\|
                    |      |
                    |
                    -
            """,
            #2 head and torso
            """
                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                    -
            """,
            #1 head
            """
                    --------
                    |      |
                    |      o
                    |      
                    |      
                    |
                    -
            """,
            #0 intial empty stage
            """
                    --------
                    |      |
                    |      
                    |      
                    |      
                     
                    -
            """,
        ]
    return stages[tries]
    
def main():
    word = getRandom()
    play(word)

    while input('do you want to play again(Y/N):').upper() == 'Y':
        word = getRandom()
        play(word)

main()
