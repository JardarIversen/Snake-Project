from time import sleep
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

start_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.busy = False

    def create_snake(self):
        for position in start_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("green")
        # new_segment.pencolor("black")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def make_busy(self):
        """self.busy = True
        sleep(0.1)
        self.busy = False"""

    def up(self):
        if self.head.heading() != DOWN and self.busy is False:
            self.head.setheading(UP)
            self.make_busy()

    def down(self):
        if self.head.heading() != UP and self.busy is False:
            self.head.setheading(DOWN)
            self.make_busy()

    def left(self):
        if self.head.heading() != RIGHT and self.busy is False:
            self.head.setheading(LEFT)
            self.make_busy()

    def right(self):
        if self.head.heading() != LEFT and self.busy is False:
            self.head.setheading(RIGHT)
            self.make_busy()
