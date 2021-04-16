import random
import art
from game_data import data

def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    return "b"

def play_game():
    print(art.logo)

    a = random.choice(data)
    b = random.choice(data)
    while b == a:
        b = random.choice(data)
        
    game_over = False
    score = 0

    while not game_over:
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}\n")

        choice = input("Which has more followers? A or B?: ").lower()
        if choice == compare(a, b):
            score += 1
            print(f"Correct! Your current score is: {score}.")
            a = b
            while b == a:
                b = random.choice(data)

        else:
            print(f"\nSorry, that's not right! Your score is {score}\n")
            game_over = True

    play_again = input("Would you like to play again? Yes or No?: ").lower()
    if play_again == "yes":
        play_game()


play_game()

