from SecretAuction_art import logo
import os
import platform


def clear_screen():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")


print(logo)

bids = {}


def find_highest(bids_dict):
    max_value = 0
    winner_name = ""
    for key in bids_dict:
        value = bids_dict[key]
        if value > max_value:
            max_value = value
            winner_name = key

    print(f"The winner is {winner_name}!!.\nWith a bid of ${max_value}")


finish = False

while not finish:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    bidders = input("Are there any other bidders?? Type (Y/N): ")
    if bidders == "N":
        finish = True
        clear_screen()
        find_highest(bids)
    elif bidders == "Y":
        clear_screen()
