from turtle import Screen
import time

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
left_score = Scoreboard(-300)
right_score = Scoreboard(300)

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()


    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.deflect()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.deflect()
        left_score.update_score()


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.deflect()
        right_score.update_score()


    if left_score.score == 3 or right_score.score == 3:
        game_active = False
        







screen.exitonclick()
