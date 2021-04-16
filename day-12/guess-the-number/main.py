import random
from .art import logo

def start_game():
    print(logo)
    difficulty = input("Which difficulty would you like? Easy, or Hard?: ")
    if difficulty.lower() == "easy":
        guesses = 10
    elif difficulty.lower() == "hard":
        guesses = 5
    return guesses

def take_guess(target):
    guess = int(input("What is your guess?: "))
    if guess == target:
        print(f"{guess} is correct! You win!")
        return True
    if guess > target:
        print(f"{guess} is too high.")
    else:
        print(f"{guess} is too low.")
    return False

def process_game():
    target_number = random.randint(1, 100)
    guesses = start_game()
    print(f"You have {guesses} guesses remaining.")
    game_won = False
    while guesses > 0:
        game_won = take_guess(target_number)
        if game_won:
            print("You win!")
            break
        guesses -=1
        print(f"You have {guesses} guesses remaining.")
    if not game_won:
        print("Sorry, you're all out of guess!")
    play_again = input("Would you like to play again?").lower()
    if play_again == "yes" or play_again == "y":
        process_game()

process_game()
