from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screenwidth = 800
screenheight = 600
screencolor = "black"

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=screenwidth, height=screenheight)
screen.bgcolor(screencolor)
screen.listen()
screen.onkeypress(r_paddle.MoveUp, "Up")
screen.onkeypress(r_paddle.MoveDown, "Down")
screen.onkeypress(l_paddle.MoveUp, "w")
screen.onkeypress(l_paddle.MoveDown, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if -280 > ball.ycor() or ball.ycor() > 280:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 100 and ball.xcor() > 320:
        ball.paddle_bounce()
    elif ball.xcor() > 350 and ball.distance(r_paddle) > 100:
        ball.goto(0, 0)
        ball.refresh()
        scoreboard.l_point()
        scoreboard.update()
        time.sleep(2)

    if ball.distance(l_paddle) < 100 and ball.xcor() < -320:
        ball.paddle_bounce()
    elif ball.distance(l_paddle) > 100 and ball.xcor() < -350:
        ball.goto(0, 0)
        ball.refresh()
        scoreboard.r_point()
        scoreboard.update()
        time.sleep(2)

screen.exitonclick()
