from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import math


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.colormode(255)
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_left, 'Left')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -260:
        ball.bounce_y()

    # Detect collision with wall
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < math.sqrt(4000) \
            or ball.xcor() < -320 and ball.distance(l_paddle) < math.sqrt(4000):
        ball.bounce_x()


screen.exitonclick()
