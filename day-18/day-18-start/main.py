from turtle import Screen, Turtle, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("lime")
tim.pensize(1)
tim.speed("fastest")
colormode(255)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def draw_shape(side_len, side_num):
    turn_angle = 360 / side_num
    tim.pencolor(random_color())
    for _ in range(side_num):
        tim.forward(side_len)
        tim.right(turn_angle)


def random_walk():
    tim.seth(randint(0, 3) * 90)
    tim.pencolor(random_color())
    tim.forward(30)


# for _ in range(1000):
#     random_walk()

def draw_spirograph(radius, gap):
    for _ in range(360 // gap):
        tim.pencolor(random_color())
        tim.circle(radius)
        tim.seth(tim.heading() + gap)

draw_spirograph(200, 3)


# for sides in range (3, 11):
#     draw_shape(100, sides)



# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)




















screen = Screen()
screen.exitonclick()
