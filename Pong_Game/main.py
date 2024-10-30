import time
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
bgcolor('black')
setup(800,600)
title('Pong Game')
tracer(0)
penup()
goto(0,300)
setheading(270)
pensize(5)

pencolor('white')
for i in range(15):
    pendown()
    fd(20)
    penup()
    fd(30)

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()
paddle1.goto(-380,0)
paddle2.goto(380,0)
score1 = ScoreBoard()
score2 = ScoreBoard()
score1.goto(-50,260)
score2.goto(50,260)

listen()
onkey(paddle1.up,'w')
onkey(paddle1.down,'s')
onkey(paddle2.up,'Up')
onkey(paddle2.down,'Down')

game_on = True
while game_on:
    update()
    time.sleep(0.1)
    score1.update_score()
    score2.update_score()
    
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    
    if ball.xcor()>375 or ball.xcor()<-375:
        ball.goto(0,0)
    
    if ball.distance(paddle1)<50 and ball.xcor() < -350:
        ball.bounce_paddle()
        score1.increase_score()
    
    if ball.distance(paddle2)<50 and ball.xcor() > 350:
        ball.bounce_paddle()
        score2.increase_score()
    

    
































exitonclick()