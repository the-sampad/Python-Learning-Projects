from turtle import Turtle

class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0,-180)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

