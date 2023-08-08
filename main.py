from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # aggiorno manualmente la scena nello schermo
    ball.move()

    # determino se la palla tocca i muri
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # determino se la palla colpisce le barre
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # determino se la palla è uscita
    if ball.xcor() > 350:
        ball.restart()
        scoreboard.update_score('l')

    if ball.xcor() < -350:
        ball.restart()
        scoreboard.update_score('r')





screen.exitonclick()