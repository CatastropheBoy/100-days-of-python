from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Super Hyper Mega Snake")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.update()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    
    snake.move()











screen.exitonclick()
