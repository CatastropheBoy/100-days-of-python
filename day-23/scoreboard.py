from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(-200, 250)
        self.color("black")
        self.speed("fastest")
        self.score = 0
        self.update_level()

    def update_level(self):
        self.score += 1
        self.clear()
        self.write(
            f"Level: {self.score}",
            align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT, font=FONT)
