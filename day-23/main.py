import time
from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_trafic()

    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.has_finished():
        scoreboard.update_level()
        player.reset()
        car_manager.increment_level()

screen.exitonclick()
