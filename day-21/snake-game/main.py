from turtle import Screen, Turtle, isvisible
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Super Hyper Mega Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_segment()
        scoreboard.update_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_active = False
        scoreboard.game_over()


    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_active = False
            scoreboard.game_over()
            break












screen.exitonclick()
