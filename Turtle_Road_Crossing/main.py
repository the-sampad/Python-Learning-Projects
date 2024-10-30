import time
from turtle import *
from tortoise import Tortoise
from car import Car
from levelboard import LevelBoard
tracer(0)
setup(600,400)
turtle = Tortoise()
level = LevelBoard()

    
listen()
onkey(turtle.up,'Up')
cars = []
game_on = True

a = 0.7
while game_on:
    update()
    time.sleep(a)
    car = Car()
    cars.append(car)
    for ele in cars:
        ele.car_move()
        if turtle.distance(ele)<19:
            game_on = False
            level.game_over()

    if turtle.ycor()>=180:
        turtle.goto(0,-180)
        a-=0.1
        level.increase_level()
    
    
    

    


exitonclick()