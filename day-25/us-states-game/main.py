from os import write
import turtle
import pandas

ALIGNMENT = "center"
FONT = ("arial", 8)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
correct_count = 0
guessed_states = []


while correct_count < 50:
    answer_state = screen.textinput(title=f"{correct_count}/50 correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        label = turtle.Turtle()
        label.ht()
        label.pu()
        label.color("black")
        label.speed("fastest")
        state_data = data[data.state == answer_state]
        label.goto(int(state_data.x), int(state_data.y))
        label.write(
            f"{answer_state}", align=ALIGNMENT, font=FONT)

        correct_count += 1
        guessed_states.append(answer_state)
        print("Correct! Guess again.")

missing_states = [state for state in states if state not in guessed_states]

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
