from turtle import *
FONT = ('Arial',18,'normal')
ALLIGNMENT = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open('data.txt','r')
        self.highscore = int(file.read())
        
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score : {self.score},  High Score = {self.highscore}',align=ALLIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        file = open('data.txt','w')
        file.write(f'{self.highscore}')
        
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align=ALLIGNMENT,font=FONT)
        
        






