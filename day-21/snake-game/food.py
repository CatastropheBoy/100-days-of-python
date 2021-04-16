from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_coord = (random.randint(-14, 14) * 20, 
                     random.randint(-14, 14) * 20)
        self.goto(ran_coord)
