from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_velocity = 10
        self.y_velocity = 10

    def move(self):
        self.new_x = self.xcor() + self.x_velocity
        self.new_y = self.ycor() + self.y_velocity
        self.goto(x=self.new_x, y=self.new_y)

    def wall_bounce(self):
        self.y_velocity *= -1

    def paddle_bounce(self):
        self.x_velocity *= -1
        self.increase_velocity()

    def refresh(self):
        if self.x_velocity > 10:
            self.x_velocity -= 2
        if self.y_velocity > 10:
            self.y_velocity -= 2
        self.x_velocity *= -1
        # self.y_velocity *= -1

    def increase_velocity(self):
        if self.x_velocity > 0:
            self.x_velocity += 2
        else:
            self.x_velocity -= 2

        if self.y_velocity > 0:
            self.y_velocity += 2
        else:
            self.y_velocity -= 2
