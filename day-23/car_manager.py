from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.difficulty = 1
        self.cars = []


    def generate_trafic(self):
        seed = random.randint(1,4)
        if seed == 1:
            self.create_car()
        for car in self.cars:
            self.drive(car)


    def create_car(self):
        start_y = random.randint(-10, 13) * 20
        car = Turtle()
        car.pu()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, start_y)
        car.setheading(180)
        self.cars.append(car)


    def drive(self, car):
        car.forward(MOVE_INCREMENT * self.difficulty)
        

    
    def increment_level(self):
        self.difficulty += 1

