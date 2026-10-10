from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_right():
    timmy.right(10)


def turn_left():
    timmy.left(10)


def screen_off():
    screen.resetscreen()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="a")
screen.onkey(fun=turn_left, key="d")
screen.onkey(fun=screen_off, key="c")
screen.exitonclick()
