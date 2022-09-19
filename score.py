from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ken = Turtle("turtle")
        self.ken.pencolor("white")
        self.ken.penup()
        self.ken.hideturtle()
        self.score = 0
        self.ken.goto(0, 270)
        self.ken.write(arg="Score: 0", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.ken.clear()
        self.ken.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.ken.goto(0,0)
        self.ken.write("GAME OVER", align=ALIGNMENT, font=("Courier", 28, "normal"))