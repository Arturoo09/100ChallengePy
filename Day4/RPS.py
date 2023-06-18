import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

option = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))


if option >= 3 or option < 0:
    print("Invalid Option!!")
else:
    print(images[option])

    computer_option = random.randint(0, 2)
    print(f"Computer option is {computer_option}")
    print(images[computer_option])

    if option == 0 and computer_option == 2:
        print("YOU WIN!!!")
    elif option == 2 and computer_option == 0:
        print("YOU LOSE!!!")
    elif computer_option > option:
        print("YOU LOSE!!!")
    elif computer_option < option:
        print("YOU WIN!!!")
    elif computer_option == option:
        print("IT's A DRAW!!!")
