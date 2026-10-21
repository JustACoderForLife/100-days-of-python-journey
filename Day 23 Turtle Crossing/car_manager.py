from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
strectch_width = 2
car_x = 320
car_y = random.randint(-260, 260)
finish_x = -320
direction = 180


class CarManager(Turtle):

    move_distance = STARTING_MOVE_DISTANCE
    move_advance = MOVE_INCREMENT

    def __init__(self):
        super().__init__(shape="square")
        self.car_y = random.randint(-260, 260)
        self.ht()
        self.up()
        self.goto(x=car_x, y=self.car_y)
        self.setheading(direction)
        self.shapesize(stretch_len=strectch_width)
        self.color(random.choice(COLORS))
        self.st()
        self.move()

    def move(self):
        if self.xcor() > finish_x:
            self.forward(CarManager.move_distance)
        else:
            self.refresh()

    def refresh(self):
        self.ht()

    @classmethod
    def increase_speed(self):
        CarManager.move_distance += CarManager.move_advance
