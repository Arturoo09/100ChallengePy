from art import logo, vs
from data import data 
import random
import os
import platform


def clear_screen():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        

def random_data():
    option = random.choice(data)
    return option


def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "A"
    else:
        return guess == "B"


def game():
    print(f"{logo}\n")
    
    game_over = False
    
    score = 0
    
    option1 = random_data()
    option2 = random_data()
    
    while not game_over:
        
        option1 = option2
        option2 = random_data()
        
        while option1 == option2:
            option1 = random_data
        
        print(f"Compare A: {option1['name']}, a {option1['description']} from {option1['country']}\n")
        print(f"{vs}\n")
        print(f"Compare A: {option2['name']}, a {option2['description']} from {option2['country']}\n")
        
        option1_score = option1['follower_count']
        option2_score = option2['follower_count']
        
        your_option = input("Who has more followers?? 'A' or 'B': ")
        
        is_correct = check_answer(your_option, option1_score, option2_score)
        
        clear_screen()
        print(f"{logo}\n")
        
        if is_correct:
            score += 1
            print(f"You're Right!!! Current Score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score {score}")     
    
game()