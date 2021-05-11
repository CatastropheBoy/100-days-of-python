from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif" width=200>'





if __name__ == "__main__":
    app.run(debug=True)