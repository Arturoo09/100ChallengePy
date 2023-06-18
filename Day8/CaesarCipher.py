from CaesarCipher_func import *

while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        clear_screen()
        print("\t\033[1;31;4mDECODE MODE\033[0m")
        print("\n")
        text = input("Message: ").lower()
        shift = int(input("Number of displacements: "))
        mode = 1

        caesar(text=text, shift=shift, mode=mode)

        print("\n")

    elif option == "2":
        clear_screen()
        print("\t\033[1;31;4mENCODE MODE\033[0m")
        print("\n")
        text = input("Message: ").lower()
        shift = int(input("Number of displacements: "))
        mode = 2

        caesar(text=text, shift=shift, mode=mode)
        print("\n")

    elif option == "0":
        print("\nExiting the program...")
        break
    else:
        print("\nInvalid option. Please choose a valid option.\n")
