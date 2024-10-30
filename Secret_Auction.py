print("""                          _________
                         [         ]
                          )_______(
                          |^^^^^^^|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )^^^^^^^(
                         [_________]
                       .-------------.
                      /_______________\ 
                      
                      """)

import os
bid_amt = 0

bid = {}

def store_bid():
    
    name = input('Name of bidder : ')
    bid_amount = int(input('Enter the bid amount : $ '))
    bid[f'{name}'] = bid_amount
    return bid
def max_bid(bid):
    mx_bid = 0
    for name in bid:
        amt = bid[name]
        if amt > mx_bid:
            mx_bid = amt
            mx_bid_name = name.title()
            mx_list = [mx_bid_name,mx_bid]
    return mx_list
i = 1
while i:

    a = input('Do you want to add a new bid to the Auction ? Yes or No :  ' ).lower()
    if a=='yes':
        b = store_bid()
        os.system('cls')
    elif a=='no':
        c = max_bid(b)
        i-=1
print(f'\nMaximum bidder of the GRAND AUCTION is {c[0]} with bid amount {c[1]}')
print('\nAll the accepted bids are : ')
for name in b:
    print(f'{name} = {b[name]}')

print('\n')
