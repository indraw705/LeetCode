import time

from ball import Ball
from paddle import Paddle
from turtle import Screen, Turtle
from scoreboard import Scorebord
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)
scoreboard = Scorebord()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'q')
screen.onkey(l_paddle.go_down, 'a')

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    screen.listen()
    ball.move()

    # Detect Collision
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect Colission with R paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()

    # Detect Right is missing ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
