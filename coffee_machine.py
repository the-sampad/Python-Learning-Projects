import os
import sys

print('''


                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'


''')
price = {'espresso':2, 'latte':5, 'cappuccino':10}
content = {'espresso':[50,25,10], 'latte':[100,75,25], 'cappuccino':[200,175,100]}
mac_water = 500
mac_milk = 500
mac_coffee = 750

mac_con = ['water','milk','coffee']
menu = list(price)
i=1
print('Menu : ')
for ele in menu:
    print(f'{ele} = Rs {price[ele]}')

while i:
    mac_report_start = [mac_water,mac_milk,mac_coffee]
    what = input('What would u like ? (Espresso, Latte, Cappuccino, Machine Report,OFF  :  ').lower()
    os.system('cls')
    print('Menu : ')
    for ele in menu:
        print(f'{ele} = Rs {price[ele]}')
    print('\nORDER : ',what)
    
    if what == 'off':
        print('Machine Turning Off')
        sys.exit()

    elif what=='espresso' or what=='latte' or what=='cappuccino':
        
        money = int(input('\nInput money = '))
        if money>=price[what]: 
            change = money - price[what]
            what_content = content[what]
            if mac_water<what_content[0] or mac_milk<what_content[1] or mac_coffee<what_content[2]:
                for i in range(3):
                    if what_content[i]>mac_report_start[i]:
                        print('Insufficient',mac_con[i],'for',what)
                print('Money Refunded =',money)        
                        
            else:  
                mac_water-=what_content[0]
                mac_milk-=what_content[1]
                mac_coffee-=what_content[2]
                print('Here is your change =  ',change)
                print('Here is your order. Freshly prepared',what,'. Have a nice day sir.')

        elif money<price[what]:
            print('Less money input. Money refunded = ',money)

    elif what=='machine report':
        print(f'Machine Report :\nWater = {mac_water} ml\nMilk = {mac_milk} ml\nCoffee = {mac_coffee} g')

    else:
        print('Invalid Input')




