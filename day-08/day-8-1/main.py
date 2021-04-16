# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Haaaaay")
    print("How")
    print("You doin'?")


def greet_with_name(name):
    print("Haaaaay")
    print("How")
    print(f"You doin', {name}?")


def greet_with(name, location):
    print(f"Hi {name}")
    print(f"What's it like in {location} right now?")

greet_with(location="Hell", name="Rush Limabaugh")