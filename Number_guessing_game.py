import os
import random
import sys
print('Welcome to the number guessing game !!')
level = input('Choose a level : Easy or Hard : ').lower()
if level=='easy':
    a=10
elif level == 'hard':
    a=5

cont = True
while cont:

    print('I am thinking of an integer between 1 and 100. Guess it.')
    num = random.randrange(1,101)
    
    for i in range(a):
        guess = int(input('Guess : '))
        if guess==num:
            print('You Win')
            play = input('Do you want to play again ? Yes or No : ').lower()
            if play == 'no':
                sys.exit()
            elif play == 'yes':
                os.system('cls')
                print('Welcome to the number guessing game !!')
            else:
                print('Invalid Input')
                sys.exit()
            
        elif guess<1 | guess>100:
            print('Out of Range')
        elif guess<num:
            print('Too Low')
        elif guess>num:
            print('Too High')
        
        if a-i == 1:
            print('You ran out of chances.\nYOU LOSE')
            print('Correct answer is  ',num)
            print('\n')
            play = input('Do you want to play again ? Yes or No : ').lower()
            if play == 'no':
                sys.exit()
            elif play == 'yes':
                os.system('cls')
                print('Welcome to the number guessing game !!')
            else:
                print('Invalid Input')
                sys.exit()
        print(f'Chances left : {a-1}')