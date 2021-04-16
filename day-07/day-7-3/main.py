import random

word_list = ["aardvark", "baboon", "camel"]
secret_word = random.choice(word_list)
word_length = len(secret_word)

display = []
for _ in secret_word:
    display += "_"

while "_" in display:
    guess = input("Please guess a letter: \n").lower()
    for i in range(word_length):
        if secret_word[i] == guess:
            display[i] = guess
            print(display)
print("You won, dawg!")
