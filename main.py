from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake.io")
screen.tracer(0)

score = Scoreboard()

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    #Detects food collision
    if snake.head.distance(food) < 5:
        food.refresh()
        score.increment_score()
        snake.extend()

    #Detects collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        score.game_over()

    # Detects collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
