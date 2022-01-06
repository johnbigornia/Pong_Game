import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# paddle dimension:
# width: 20, height: 100, x_pos:350, y_pos: 0

# ball dimension:
# width: 20, height: 20, xpos: 0,y_pos: 0

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# cancels animations but proceeds to execute instructions
screen.tracer(0)

left_paddle = Paddle(x_cord=-350)
right_paddle = Paddle(x_cord=350)

ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

scoreboard = Scoreboard()

game_on = True

while game_on:
    # shows the end result after code executes
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()

    # detecting collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # detecting point collision
    if ball.xcor() > 380:
        ball.ball_reset(winner="right")
        scoreboard.left_point()

    # detecting point collision
    if ball.xcor() < -380:
        ball.ball_reset(winner="left")
        scoreboard.right_point()


screen.exitonclick()
