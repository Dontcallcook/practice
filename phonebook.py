import os
import time



def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def prompt(message):
    print(f"---> {message}")

def phone_book():
    phonebook = {
    }

    name_list = []

    def welcome_message():
        prompt("Welcome to Phone Book")
    
    def flash_message(message):
        clear_screen()
        prompt(message)
        time.sleep(1)
        clear_screen()
    
    def display_menu():
        prompt("1) Add a contact 2) Delete a contact 3) Edit a contact 4) View contacts 5) Exit")
    
    def get_choice():
        choice = input("")
        return choice
    
    def resolve_menu_choice(choice):
        if choice == "1": # add contact
            add_contact()
        elif choice == "2": # remove contact
            rem_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4": # display contact
            display_contacts()
            prompt("")
            prompt("Press 'enter' to continue.")
            input()
            clear_screen()
        elif choice == "5":
            prompt("Thanks for using phonebook!")
            exit()
    
    def not_valid_number(number):
        if number.isdigit() or (number.startswith("+") and number[1::].isdigit()):
            return False
        return True
        
    def check_valid_number(number):
        while not_valid_number(number):
            clear_screen()
            prompt("Please type a valid number:")
            number = input()
        return number
    
    def add_contact():
        prompt("Name: ")
        name = input().capitalize()
        prompt("Number: ")
        number = input()
        number = check_valid_number(number)
        phonebook[name] = number
        name_list.append(name)
        flash_message("Contact added successfully!")
    
    def rem_contact():
        display_contacts()
        prompt("Which contact would you like to remove?")
        choice = input().capitalize().strip(" ,.:;!?-")
        if choice.isdigit():
            del phonebook[name_list[int(choice) -1]]
        elif choice in phonebook:
            del phonebook[choice]
        flash_message("Contact removed successfully!")
    
    def edit_contact():
        prompt("Which contact would you like to update the name?")
        display_contacts()
        prompt("")
        choice = input()
        if choice.isdigit():
            clear_screen()
            prompt(f"Enter {name_list[int(choice) - 1]}'s new number:")
            number = input()
            number = check_valid_number(number)
            phonebook[name_list[int(choice) - 1]] = number
            flash_message("Contact updated successfully!")
        elif choice.strip(" .,:;!?-").capitalize() in phonebook:
            clear_screen()
            prompt(f"Enter {choice}'s new number:")
            number = input()
            number = check_valid_number(number)
            phonebook[choice] = number
    
    def display_contacts():
        if not phonebook:
            prompt("Your phonebook is empty!")
        for i, name in enumerate(phonebook):
            prompt(f"{i + 1}. {name}: {phonebook[name]}")
    
    
    welcome_message()
    display_menu()
    user_choice = get_choice()
    clear_screen()
    resolve_menu_choice(user_choice)
    
    while True:
        prompt("What would you like to do next?")
        display_menu()
        user_choice = get_choice()
        clear_screen()
        resolve_menu_choice(user_choice)

phone_book()
