from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 16)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.score = -1
        with open("data.txt", "r") as data:
            self.hi_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.hi_score}",
            align=ALIGNMENT, font=FONT)


    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 250)
    #     self.write(
    #         f"GAME OVER\nFinal Score:{self.score}",
    #         align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open ("data.txt", "w") as data:
                data.write(str(self.score))
        self.score = -1
        self.update_score()
