import random



def high_low():
    a = random.choice(list(superhero_popularity))
    print(f'A = {a}')
    stop = False
    count = 0
    chalo = True
    while not stop:
        b = random.choice(list(superhero_popularity))
        if b==a:
            b = random.choice(list(superhero_popularity))
        elif b!=a:
            stop = True
    while chalo:
        
        print(f'B = {b}')
        who_is_more = input('Who is more popular ? A or B  : ').lower()
        if who_is_more == 'a':
            if superhero_popularity[a] > superhero_popularity[b]:
                print('You are CORRECT')
                count+=1
                print(f'Your Score = {count}')
                a = b
                i=1
                while i:
                    b = random.choice(list(superhero_popularity))
                    if b==a:
                        b = random.choice(list(superhero_popularity))
                    elif b!=a:
                        i-=1
                    print(b)
                print (f'A = {a}')
            else:
                print('WRONG')
                print(f'Your Score = {count}')
                chalo = False
        
        if who_is_more == 'b':
            if superhero_popularity[b] > superhero_popularity[a]:
                print('You are CORRECT')
                count+=1
                print(f'Your Score = {count}')
                a = b
                i=1
                while i:
                    b = random.choice(list(superhero_popularity))
                    if b==a:
                        b = random.choice(list(superhero_popularity))
                    elif b!=a:
                        i-=1
                print (f'A = {a}')
            else:
                print('WRONG')
                print(f'Your Score = {count}')
                chalo = False
        

superhero_popularity = {'Spider-Man':57, 'Wonder Woman':15, 'Batman':11, 'Iron Man':10, 'Superman':6, 
'Captain America':4, 'Aquaman':4, 'Hulk':3, 'Wanda Maximoff':2, 'Groot':1}


import os
import sys
stop_1 = False
while not stop_1:
    high_low()
    play = input('Do you want to play again ? Yes or No : ').lower()
    if play == 'no':
        sys.exit()
    elif play == 'yes':
        os.system('cls')
        print('Welcome to the High Low Game !!')
            
    else:
        print('Invalid Input')
        sys.exit()

