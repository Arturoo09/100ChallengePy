import random
from GuessTheNumber_art import logo

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

HARD_LIVES = 5
EASY_LIVES = 10

def choose_difficulty():
    difficulty = input("Choose a difficulty (hard/eassy): ")
    if difficulty == "hard":
        return HARD_LIVES
    else:
        return EASY_LIVES
    
def compare(guess, answer, lives):
    if guess == answer:
        print(f"You WIN!!! The answer was {answer}.")
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print("Too high.")
        return lives - 1

def game():
    print(f"{logo}\n")

    print("WELCOME TO THE NUMBER GUESSING GAME!!")
    print("I'm thinking a number between 1 - 100.")
        
    the_number = random.randint(1,100)
    lives = choose_difficulty()

    guess = 0
    
    while guess != the_number:
        
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        
        lives = compare(guess, the_number, lives)
        if lives == 0:
            print(f"You've run out of guesses, you lose.\nThe answer was {the_number}")
            return
        elif guess != the_number:
            print("Guess again.")
    
game()    