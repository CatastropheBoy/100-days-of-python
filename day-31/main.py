from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
card = None


def new_word():
    global timer, card 

    window.after_cancel(timer)
    canvas.itemconfig(card_side, image=card_front)
    card = choice(to_learn)
    french_def = card["French"]
    canvas.itemconfig(word_language, text="French", fill="black")
    canvas.itemconfig(word_body, text=french_def, fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    english_def = card["English"]
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(word_language, text="English", fill="white")
    canvas.itemconfig(word_body, text=english_def, fill="white")


def remove_word():
    to_learn.remove(card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    new_word()


try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_side = canvas.create_image(400, 263, image=card_front)
word_language = canvas.create_text(400, 160, text="", fill="black", font=("Ariel", 40, "italic"))
word_body = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_button_image, highlightthickness=0, command=new_word)
x_button.grid(row=1, column=0)

check_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_button_image, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)

timer = window.after(3000, flip_card)


new_word()

window.mainloop()