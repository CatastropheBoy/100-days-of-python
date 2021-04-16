import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
lives = 6

display = []
for _ in secret_word:
    display += "_"

game_over = False
while not game_over:
    guess = input("Please guess a letter: \n").lower()
    for i in range(word_length):
        if secret_word[i] == guess:
            display[i] = guess
    print(f"{''.join(display)}")

    if "_" not in display:
        game_over = True
        print("You won, dawg!")

    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose, broh!")

    print(stages[lives])
