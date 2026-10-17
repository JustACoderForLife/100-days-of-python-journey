from turtle import Turtle

paddle_shape = "square"
paddle_color = "white"


# def MoveUp():
#     new_y = paddle.ycor() + 20
#     paddle.goto(x=initial_paddle_x, y=new_y)


# def MoveDown():
#     new_y = paddle.ycor() - 20
#     paddle.goto(x=initial_paddle_x, y=new_y)


# paddle = Turtle(shape=paddle_shape)
# paddle.color(paddle_color)
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(x=initial_paddle_x, y=initial_paddle_y)


class Paddle(Turtle):

    def __init__(self, coordinates: tuple):
        super().__init__()
        self.shape(paddle_shape)
        self.color(paddle_color)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def MoveUp(self):
        self.new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=self.new_y)

    def MoveDown(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
