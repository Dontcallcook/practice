import os
import time

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def prompt(message):
    print(f"---> {message}")

def menu_select():
    prompt("What should we do next?")
    prompt(" 1) Add a new task 2) Remove a task 3) View current tasks 4) Exit")
    choice = input()
    return choice

def menu_select_not_valid(selection):
    return selection not in ["1", "2", "3", "4"]
    
def get_task():
    task = input().strip().capitalize()
    return task

def add_task(task):
    task_list.append(task)

def duplicate_check(task):
    return task in task_list

def display_tasks(task_list):
    prompt("")
    for index, task in enumerate(task_list):
        prompt(f"{index + 1}: {task}")

def remove_not_valid(selection):
    for index, task in enumerate(task_list):
        if selection == str(index + 1) or selection == task:
            return False
    return True

def task_removal(selection):
    for index, task in enumerate(task_list):
        try:
            if int(selection) == (index + 1):
                task_list.pop(index)
        except ValueError:
            if selection == task:
                task_list.pop(index)

task_list = []

def task_master():
    prompt("Welcome to Task Master!")
    
    prompt("What's the first task you would like to add to your list?")
    task = input().strip().capitalize()
    add_task(task)
    clear_screen()
    
    while True:
        choice = menu_select()
        while menu_select_not_valid(choice):
            clear_screen()
            prompt("Action not valid!")
            time.sleep(1)
            clear_screen()
            choice = menu_select()
        
        if choice in ["1"]: # add tasks
            clear_screen()
            prompt("Ok! What task would you like to add?")
            task = get_task()
            if duplicate_check(task):
                clear_screen()
                prompt("That task is already in the list!")
                time.sleep(1)
                clear_screen()
                continue
            add_task(task)
            clear_screen()
            prompt("Task added successfully!")
            time.sleep(1)
            clear_screen()
        
        if choice in ["2"]: # remove tasks
            clear_screen()
            if not task_list:
                prompt("There are no tasks to remove!")
                time.sleep(1)
                clear_screen()
                continue
            prompt("No problem! Which task should we remove?")
            display_tasks(task_list)
            task = get_task()
            
            while remove_not_valid(task):
                clear_screen()
                prompt("That task is not in the list! "
                "Please choose from your current task list:")
                display_tasks(task_list)
                task = get_task()

            task_removal(task)
            clear_screen()
            prompt("Task removed successfully!")
            time.sleep(1)
            clear_screen()
        
        if choice in ["3"]: # display tasks
            clear_screen()
            if not task_list:
                clear_screen()
                prompt("No tasks currently assigned!")
                time.sleep(1)
                clear_screen()
                continue
            prompt("Great! Here are your current tasks:")
            display_tasks(task_list)
            prompt("")
            prompt("Press 'enter' to continue...")
            input()
            clear_screen()
        
        if choice in ["4"]: # exit
            clear_screen()
            prompt("Ok! Thanks for using Task Master")
            break

task_master()
