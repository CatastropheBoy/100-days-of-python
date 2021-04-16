from turtle import Turtle, colormode, mode, Screen
import random

tim = Turtle()
mode("logo")
tim.hideturtle()
tim.speed("fastest")
colormode(255)


rgb_colors = [(201, 164, 112), (152, 75, 50), (221, 201, 138),
              (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75)]

def draw_hirst(rows, cols):
    tim.pu()
    start_offset = (50 * rows // 2) * -1
    start_pos = (start_offset, start_offset)
    tim.setpos(start_pos)
    for row in range(rows):
        tim.forward(50 * row)
        tim.right(90)
        for _ in range(cols):
            tim.dot(20, random.choice(rgb_colors))
            tim.forward(50)
        tim.setpos(start_pos)
        tim.seth(0)
    tim.pd()

draw_hirst(15, 15)
screen = Screen()
screen.exitonclick()


