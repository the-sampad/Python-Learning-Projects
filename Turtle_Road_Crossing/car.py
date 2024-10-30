COLORS = ['red','blue','green','yellow','magenta','brown','sea green']
import time
import random
from turtle import *

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.color(random.choice(COLORS))
        
        self.goto(290,random.randint(-150,150))

    def car_move(self):
        self.backward(20)





