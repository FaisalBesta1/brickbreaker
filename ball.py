from turtle import Turtle

STARTER_COORDS = (0, -236)

'''
Class to create the ball, cause it to move and change direction once met with an obstacle.
'''

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.goto(STARTER_COORDS)

    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset_pos(self):
        self.setpos(STARTER_COORDS)
        self.y_bounce()
