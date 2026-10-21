from turtle import Turtle

FONT = ("Courier", 24, "normal")
destination = (-260, 272)


class Scoreboard(Turtle):

    def __init__(self, visible=False):
        super().__init__(visible=visible)
        self.score = 0
        self.up()
        self.goto(destination)
        self.write(arg="Level: 0", font=FONT)

    def reset(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", font=FONT)
