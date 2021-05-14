from flask import Flask
import random

number = random.randint(0,9)
app = Flask(__name__)



@app.route('/')
def hello():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif" width=200>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < number:
        return "Your guess is too low."
    elif guess > number:
        return "Your guess is too high."
    else:
        return "Your guess is correct."


if __name__ == "__main__":
    app.run(debug=True)