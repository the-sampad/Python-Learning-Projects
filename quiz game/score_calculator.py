class ScoreCalculator:
    def __init__(self,score,lives):
        self.score = score
        self.lives = lives
    def score_calc(self,check):
        if check == True:
            self.score+=1

        return self.score
    
    def life_calc(self,check):
        if check == False:
            self.lives-=1

        return self.lives
