from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score1()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 16, "normal"),
        )

    def increase(self):
        self.score += 1
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 16, "normal"),
        )

    # def game_over(self):
    #     self.goto(x=0, y=40)
    #     self.write(arg=f"Game Over!", align="center", font=("Arial", 16, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_hs()
        self.score = 0
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 16, "normal"),
        )

    def high_score1(self):
        try:
            with open(file="data.txt", mode="r") as file:
                content = file.read().strip()
                self.high_score = int(content) if content else 0
        except FileNotFoundError:
            self.high_score = 0

    def update_hs(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
