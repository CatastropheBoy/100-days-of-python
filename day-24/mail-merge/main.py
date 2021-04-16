#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/names/invited_names.txt", "r") as f:
    names = f.readlines()
    for name in names:
        name = name.strip()

for name in names:
    with open("./input/letters/starting_letter.txt") as f:
        letter = f.read()
        new_name = name.strip()
        letter = letter.replace("[name]", new_name)
        with open(f"./output/readytosend/letter_for_{new_name}.txt", "w") as o:
            o.write(letter)

