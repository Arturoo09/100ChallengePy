import os
import platform

def clear_screen():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

def show_menu():
    print("╔════════════════════════════════════╗")
    print("║             MAIN MENU              ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Decode                         ║")
    print("║  2. Encode                         ║")
    print("║  0. Exit                           ║")
    print("╚════════════════════════════════════╝")
    
def caesar(text, shift, mode):
    cipher_text = ""
    
    if mode == 1:
        shift *= -1
        mode_name = "decoded"
    else:
        mode_name = "encoded"
    
    for char in text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
        
    print(f"The {mode_name} message is: {cipher_text}")