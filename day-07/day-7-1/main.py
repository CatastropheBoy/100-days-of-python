import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

secret_word = random.choice(word_list)
guess = input("Please guess a letter: \n").lower()
for letter in secret_word:
    if letter == guess:
        print("Yeah broh!")
    else:
        print("Nah dawg!")