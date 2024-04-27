# Write a program where the user can enter a list of numbers (one by one) and then prints out the largest number from that list.
import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

number_list = []

while True:
    print("1) add a number")
    print("2) process list")
    choice = input()
    if choice == "1":
        clear_screen()
        number = int(input(("Type your number: ")))
        number_list.append(number)
    elif choice == "2":
        clear_screen()
        largest = max(number_list)
        print(f"Here is your list:")
        print(number_list)
        print(f"This is the largest number: {largest}.")
        break
    else:
        clear_screen()
        print("That's not a valid choice!")
    