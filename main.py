from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 900)
screen.bgcolor('black')
screen.tracer(0)
segments = []

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()