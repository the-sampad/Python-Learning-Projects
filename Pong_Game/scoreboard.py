from turtle import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        
    def update_score(self):
        self.write(f'{self.score}',align = 'center', font = ('Arial',25,'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    