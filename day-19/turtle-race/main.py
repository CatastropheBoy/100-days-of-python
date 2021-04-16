from turtle import Turtle, Screen, penup
import random

screen = Screen()
screen.setup(width=500, height=400)

color_index = ["red", "blue", "lime", "purple", "yellow"]
height_index = 100
turtles = []
for turtle in range(5):
    turtle = Turtle(shape="turtle")
    color = color_index.pop(random.randint(0,len(color_index) - 1))
    turtle.color(color)
    turtle.pu()
    turtle.goto(-230, height_index)
    height_index -= 50
    turtles.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")

is_race_on = True
while is_race_on:
    for turtle in turtles:
        ran_dist = random.randint(0, 10)
        turtle.forward(ran_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"The {winner} turtle has finished first!")
            if winner == user_bet:
                print("You've won!")
            else:
                print("You've lost!")
            break





screen.exitonclick()
