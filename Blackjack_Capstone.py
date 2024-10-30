import sys
import random
import os
# Blackjack Capstone



def blackjack():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = cards+cards+cards+cards
    
    bet_amount = int(input('Enter bet amount : '))
    stop = False
    while not stop:
        player_cards = random.sample(cards,2)
        for ele in player_cards:
            cards.remove(ele)
        dealer_2_cards = random.sample(cards,2)
        for ele in dealer_2_cards:
            cards.remove(ele)
        print(f'Player cards : {player_cards}')
        print(f'Dealer cards : {dealer_2_cards[0]}, Hidden')
        i = 2
        while i:
            if i == 2:
                i-=1
            if sum(player_cards)>21:
                print('YOU LOSE')
                sys.exit()
            elif sum(player_cards) == 21:
            
                print(f'Dealer cards shown : {dealer_2_cards[0]}, {dealer_2_cards[1]}')
                if sum(dealer_2_cards)<21:
                    print(f'YOU WIN. Winning prize {2*bet_amount}')
                elif sum(dealer_2_cards)==21:
                    print('Game Tied')
                i-=1
                play_another = input('Do you want to play another game ? Yes or No :  ').lower()
                if play_another == 'no':
                    sys.exit()
                elif play_another == 'yes':
                    stop=False
                    os.system('cls')
                else:
                    print('Invalid Input')
                    sys.exit()
            elif sum(dealer_2_cards) < 21:
                h_or_d = input('Do you want to Hit or Deal ? ').lower()
                if h_or_d=='hit':
                    print(f'Dealer cards shown : {dealer_2_cards[0]}, {dealer_2_cards[1]}')
                    if sum(player_cards)>sum(dealer_2_cards):
                        print(f'YOU WIN. Winning prize {2*bet_amount}')
                    elif sum(player_cards)<sum(dealer_2_cards):
                        print('YOU LOSE')
                    elif sum(player_cards)==sum(dealer_2_cards):
                        print('Game Tied')
                    i-=1
                    play_another = input('Do you want to play another game ? Yes or No :  ').lower()
                    if play_another == 'no':
                        sys.exit()
                    elif play_another == 'yes':
                        stop=False
                        os.system('cls')
                    else:
                        print('Invalid Input')
                        sys.exit()
                    
                elif h_or_d == 'deal':
                    chosen_card = random.choice(cards)
                    cards.remove(chosen_card)
                    player_cards.append(chosen_card)
                    print(f'Player cards : {player_cards}')
                    print(f'Dealer cards shown : {dealer_2_cards[0]}, {dealer_2_cards[1]}')

        

play = input('Do you want to play Blackjack Game ? : ').lower()
if play == 'no':
    sys.exit()
elif play == 'yes':
    blackjack()
else:
    print('invalid input')
    sys.exit()





