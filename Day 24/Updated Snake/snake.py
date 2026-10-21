from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(right)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(up)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(left)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(down)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
