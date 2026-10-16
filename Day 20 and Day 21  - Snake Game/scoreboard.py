from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x = 0, y = 260)
        self.write(arg = f"Score: 0", align = "center", font=('Arial', 16, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Score: {self.score}", align = "center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(x = 0, y = 40)
        self.write(arg = f"Game Over!", align = "center", font=('Arial', 16, 'normal'))
