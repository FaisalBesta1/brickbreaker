from turtle import Turtle
from brick import Brick

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

'''
Class to keep track of the score and high score 
'''


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = ""
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()
        super().penup()
        super().hideturtle()
        super().goto(0, 275)
        super().color("black")
        super().speed(0)
        self.score_file()

    def score_file(self):
        super().clear()
        super().write(f"Score = {self.score}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                self.score_file()
        self.score = 0

    def game_over(self):
        super().clear()
        super().write(f"GAME OVER, Score = {self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 100
        self.score_file()




