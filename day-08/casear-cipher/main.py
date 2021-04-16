from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    output = ""
    if shift > 26:
        shift = shift % 26

    for i in range(len(text)):
        letter = text[i]
        if letter not in alphabet:
            output += letter
            continue
        if direction.lower() == "encode":
            offset = alphabet.index(letter) + shift
            if offset > 25:
                offset -= 26
        elif direction.lower() == "decode":
            offset = alphabet.index(letter) - shift
            if offset < 0:
                offset += 26
        letter = alphabet[offset]
        output += letter
    print(f"The {direction}d text is {output}")

    prompt_restart = input("Would you like to restart? Yes or No?\n")
    if prompt_restart.lower() == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)

caesar(text, shift, direction)
