from turtle import Turtle

STARTING_POSITIONS = [(-500, 275), (-475, 275), (-450, 275)]


'''
Class to keep track of lives
'''

class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = []
        self.hideturtle()
        self.number_of_lives()

    def number_of_lives(self):
        for i in range(3):
            lives = Turtle("turtle")
            lives.color("black")
            lives.penup()
            lives.setpos(STARTING_POSITIONS[i])
            self.lives.append(lives)

    def lose_life(self):
        self.lives[-1].color("dark gray")
        self.lives.remove(self.lives[-1])



