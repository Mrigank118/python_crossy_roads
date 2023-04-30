from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-140, 250)
        self.hideturtle()
        self.count = 0
        self.color("black")
        self.write(f"Level: {self.count} ", align="right", font=FONT)


    def increase_level(self):
        self.count += 1
        self.clear()
        self.write(f"Level: {self.count} ", align="right", font=FONT)

    def game_over(self):
        self.clear()
        self.write("Game Over", align="right", font=FONT)


