from turtle import *

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color('white')

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
       
    
        
        

