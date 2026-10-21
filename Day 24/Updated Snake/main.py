from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gonna Make it - Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    if (
        snake.segments[0].xcor() > 290
        or snake.segments[0].xcor() < -290
        or snake.segments[0].ycor() > 290
        or snake.segments[0].ycor() < -290
    ):
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
