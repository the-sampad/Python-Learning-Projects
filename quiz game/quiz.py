# Quiz Game
import os
import sys

from questions_and_answers import QuestionsAndAnswers
from score_calculator import ScoreCalculator
def welcome():
    print('''\033[32m
            ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              """
    

    WELCOME TO THE QUIZ !!!! LET'S HAVE SOME BRAIN DRAINS !!!!\033[m
    
    ''')
def play_or_n():
    play = input('\nDo you want to play again ? Yes or No :  ').lower()
    if play == 'yes' or 'y':
        stop = False
        os.system('cls')
    elif play == 'no' or 'n':
        stop = True
        sys.exit()
    else:
        print('Invalid Input')
        sys.exit()
    return stop

stop = False


while not stop:
    welcome()
    qna = QuestionsAndAnswers()
    score = 0
    lives = 4
    for i in range(len(qna.quesions)):
        
        scr = ScoreCalculator(score,lives)
        question = qna.ask_question(i)
        answer = input(question)
        check = qna.is_answer_correct(answer)
        score = scr.score_calc(check)
        lives = scr.life_calc(check)
        print(f'Score = {score}/{i+1} and  lives remaining = {lives}')
        print('\n')
        if lives == 0:
            print('You ran out of lives.')
            break
        
    
    stop = play_or_n()




    

    

