from turtle import Turtle


WIDTH = 10
LEN = 1

STARTING_POS = (0, -260)

'''
Class to create the paddle 
'''

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        super().shape("square")
        super().color("white")
        super().penup()
        super().shapesize(stretch_wid=WIDTH, stretch_len=LEN)
        super().goto(STARTING_POS)
        super().setheading(90)

    def right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def reset_pos(self):
        self.goto(STARTING_POS)

