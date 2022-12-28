from turtle import Turtle, Screen
from ball import Ball
from brick import Brick
from lives import Lives
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("dark gray")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
brick = Brick()
scoreboard = Scoreboard()
ball = Ball()
lives = Lives()
green_line = brick.green_line
yellow_line = brick.yellow_line
red_line = brick.red_line

# Checks for key input to move the paddle

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

sleep = 0.03
level = 1

game_is_on = True
while game_is_on and level <= 3:
    time.sleep(sleep)
    ball.move()
    screen.update()

    # When collisions with the wall happen, prevents the ball from leaving the screen

    if ball.xcor() < -575 or ball.xcor() > 575:
        ball.x_bounce()

    if ball.ycor() > 275:
        ball.y_bounce()

    # Detects paddle collision

    if ball.distance(paddle) < 110 and ball.ycor() < -240:
        # On the right side of the screen, if the ball collides with the right paddle it will change the x direction.
        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                ball.x_bounce()
                ball.y_bounce()
            else:
                ball.y_bounce()

        # On the left side of the screen, if the ball collides with the left side of the paddle, change the x direction.
        elif paddle.xcor() < 0:
            if ball.xcor() < paddle.xcor():
                ball.x_bounce()
                ball.y_bounce()
            else:
                ball.y_bounce()

        # Middle of the screen, if the ball collides with paddle, change the x direction.
        else:
            if ball.xcor() > paddle.xcor():
                ball.x_bounce()
                ball.y_bounce()
            elif ball.xcor() < paddle.xcor():
                ball.x_bounce()
                ball.y_bounce()
            else:
                ball.y_bounce()

    # Checks collision with the bricks and adds onto the current score and destroys the brick

    for green in green_line:
        if ball.distance(green) < 25 and ball.ycor() > -20:
            ball.y_bounce()
            brick.destroy(green)
            scoreboard.score_increase()

    for yellow in yellow_line:
        if ball.distance(yellow) < 25 and ball.ycor() < 190:
            ball.y_bounce()
            brick.destroy(yellow)
            scoreboard.score_increase()

    for red in red_line:
        if ball.distance(red) < 25 and ball.ycor() < 390:
            ball.y_bounce()
            brick.destroy(red)
            scoreboard.score_increase()

    # Failure to hit the ball causes player to lose a life. The paddle and ball will reset at the middle of the
    # screen

    if ball.ycor() < -270:
        ball.reset_pos()
        lives.lose_life()
        paddle.reset_pos()

    # Creates new level

    if len(red_line) == 0 and len(green_line) == 0 and len(yellow_line) == 0:
        brick.create_green_line()
        brick.create_red_line()
        brick.create_yellow_line()
        ball.reset_pos()
        paddle.reset_pos()
        level += 1
        sleep -= 0.01

    # Checks for lives, if there is no more lives the game will end

    if len(lives.lives) == 0:
        scoreboard.game_over()
        scoreboard.reset()
        game_is_on = False

screen.exitonclick()


