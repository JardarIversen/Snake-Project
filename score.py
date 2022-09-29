from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

