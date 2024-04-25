import random

guess_count = 0

def prompt(message):
    print(f"---> {message}")

def valid_guess(user_guess):
    return user_guess.isdigit() and int(user_guess) in range(1, 101)

def get_guess():
    prompt("What's your guess?")
    guess = input()
    
    while valid_guess(guess) is False:
        prompt("Your input is invalid. "
        "Please type a number between 1 and 100:")
        guess = input()
    
    guess = int(guess)
    return guess

def play_again_valid(choice):
    if (choice not in ['y', 'yes', 'ye', 'yea', 'yeah']
    and choice not in ['n', 'no', 'nope']):
        return False
    return True

def guess_count_increment(guess_count):
    guess_count += 1

while True:
    guess_count = 0
    number = random.randrange(1, 101)
    
    guess = get_guess()
    guess_count += 1
    
    while True:
        if guess < number:
            prompt("That's too low.")
            guess = get_guess()
            guess_count += 1
        elif guess > number:
            prompt("That's too high.")
            guess = get_guess()
            guess_count += 1
        else:
            prompt(f"Well done! You got it in {guess_count} guesses!")
            break

    prompt("Type 'yes' to play again or 'no' to exit:")
    play_again_choice = input().strip().lower()
    
    while play_again_valid(play_again_choice) is False:
        prompt("""Your choice is not valid.
        Please type 'yes' or 'no':""")
        play_again_choice = input()
    
    if play_again_choice.startswith("y"):
        continue
    elif play_again_choice.startswith("n"):
        prompt("Ok, thanks for playing!")
        break