import random
from hangman_words import word_list
from hangman_art import stages, logo

secret_word = random.choice(word_list)
word_length = len(secret_word)
lives = 6
print(logo)
display = []
for _ in secret_word:
    display += "_"
print(display)

game_over = False
guesses = []
while not game_over:
    guess = input("Please guess a letter: \n").lower()
    if guess in guesses:
        print(f"You've already guessed {guess}")
        continue
    guesses += guess

    for i in range(word_length):
        if secret_word[i] == guess:
            display[i] = guess
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You won, dawg!")

    if guess not in secret_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose, broh!")
            print(f"The word was {secret_word}")
    print(stages[lives])
