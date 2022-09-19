from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.7)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-14, 14) * 20
        random_y = randint(-14, 14) * 20
        self.goto(random_x, random_y)
