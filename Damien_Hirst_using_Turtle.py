import random
from turtle import *
colormode(255)
speed(100)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
penup()
back(250)
left(90)
back(250)
right(90)
penup()
speed('fastest')

for i in range(10):
    for j in range(9):
        color(random_color())
        dot(20)
        forward(50)
        color(random_color())
        dot(20)
        
    
    left(90)
    forward(50)
    left(90)
    forward(9*50)
    right(180)
    
hideturtle()


exitonclick()
