import random
import os
from hangman_words import word_list
from hangman_art import *

print(logo)
print(f"\n\n{name}")

lives = 6

the_word = random.choice(word_list)

blanks = []
for blank in range(0, len(the_word)):
    blanks.append("_")

print(f"\nHere is the template: {' '.join(blanks)}")

end_game = False

while not end_game:

    guess = input("\nGuess a letter: ").lower()

    os.system("cls")

    for position in range(len(the_word)):
        letter = the_word[position]
        if letter == guess:
            blanks[position] = letter

    if guess not in the_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("Out of lives!! \nYOU LOSE!!")
            print(f"\nThe chosen word was: {the_word.upper()}")

    print(f"\nYour guess: {' '.join(blanks)}")

    if "_" not in blanks:
        end_game = True
        print("\nYOU WIN!")

    print("\n" + stages[lives])
