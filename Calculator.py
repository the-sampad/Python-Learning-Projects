
import os
def calculate(x,y,op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        return x/y
    



i = 1
while i:
    print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')

    a = float(input('Enter a number : '))
    k = 1
    while k:
        
        oper = input('\n+\n-\n*\n/\nWhich of the above operations you want to perform ? ')
        b = float(input('Enter another number : '))
        res = calculate(a,b,oper)
        
        print(f'\nresult = {res}')
        print('\n')
        cont = input(f'Enter Y if you want to continue with {res}\nEnter N if want to start a fresh calculator\nEnter END to stop  :  ').lower()
        if cont == 'y':
            k=k
            a=res
        elif cont == 'n':
            k-=1
            os.system('cls')
        elif cont == 'end':
            i-=1
            k-=1






























