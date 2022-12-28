from turtle import Turtle

COORDS = [i for i in range(-525, 550, 50)]
Y_COORDS = [0, 100, 200]

'''
Class to create the bricks and destroy the bricks
'''


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.green_line = []
        self.yellow_line = []
        self.red_line = []
        self.create_line("green", Y_COORDS[0])
        self.create_line("yellow", Y_COORDS[1])
        self.create_line("red", Y_COORDS[2])
        self.hideturtle()

    def create_line(self, colour, y_coords):
        for i in range(22):
            brick = Turtle("square")
            brick.penup()
            brick.color(f"{colour}")
            brick.shapesize(stretch_wid=1, stretch_len=2.25)
            brick.setpos(COORDS[i], y_coords)
            if colour == "green":
                self.green_line.append(brick)
            elif colour == "yellow":
                self.yellow_line.append(brick)
            elif colour == "red":
                self.red_line.append(brick)

    def destroy(self, brick):
        brick = brick
        brick.color("dark gray")
        if brick in self.red_line:
            self.red_line.remove(brick)
        elif brick in self.green_line:
            self.green_line.remove(brick)
        elif brick in self.yellow_line:
            self.yellow_line.remove(brick)
