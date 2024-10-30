import time
from snake import Snake
from turtle import *
from food import Food
from score_board import ScoreBoard
bgcolor('black')
setup(width = 600, height = 600)
title('Snake Game')
tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
listen()
onkey(snake.up, 'Up')
onkey(snake.down, 'Down')
onkey(snake.right, 'Right')
onkey(snake.left, 'Left')
    
game_on = True
while game_on:
    update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



    










exitonclick()


