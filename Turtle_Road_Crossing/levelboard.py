
from turtle import *

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-240,170)
        self.update_level()
    
    def update_level(self):
        self.write(f'Level = {self.level}',align='center',font=('Arial',17,'normal'))
    
    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align='center',font=('Arial',25,'normal'))