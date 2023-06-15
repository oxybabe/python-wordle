import sys
from termcolor import colored, cprint
import random
word_bank = ["crane", "black", "train", "candy", "buzzy", "apart"]
print(colored("Welcome to Wordle!", "blue"))
secret_word = random.choice(word_bank)
word_to_guess = list(secret_word)
print(secret_word)
guess_word = ["", "", "", "", ""] #splitting the letters in each word into a string in an array
attempt = 0
correct_letters=0

while attempt < 6:
        guess = input()
        guess_word = list(guess)
        
        for i in range(5):
                if guess_word[i] == word_to_guess[i]:
                        print(colored(guess_word[i], "green"), end=" ") #if the letter matched the guessed word letter & in the correct index, it turns green
                        correct_letters += 1
                elif guess_word[i] in word_to_guess:
                        print(colored(guess_word[i], "yellow"), end=" ") #if the letter matched the guessed word & not in the correct indexr, it turns yellow
                else:
                        print(colored(guess_word[i], "grey"), end=" ")
                        
        attempt += 1
        if correct_letters == 5:
                print("You are a wordle champ!")
                break
        if attempt == 6:
                print("You are out of turns! The correct word was", "" .join(secret_word))
        
        
        #Use the “end” parameter with the print() function in Python to print horizontally.