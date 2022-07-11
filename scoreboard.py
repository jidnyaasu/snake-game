from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
FONT1 = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt", "r") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # if self.score > self.high_score:
        #     self.high_score = self.score
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()
        # self.goto(0, 0)
        # self.write(f"Game Over!", align=ALIGNMENT, font=FONT1)
