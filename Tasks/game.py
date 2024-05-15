import random

def print_ascii():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|___
      |  \/ K|                            _/ |                
      '------'                           |__/ 
    
""")
    
#random card numbers
def deal_cards():
    return random.randint(2, 11)

#card function
def calculate(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        score -= 1
    return  score

#display function
def display(player_cards, opponent_cards, player_score, show_opponent_card=False):
    opponent_card = opponent_cards[0] if show_opponent_card else 'X'
    opponent_score = calculate(opponent_cards) if show_opponent_card else opponent_cards[0]

    print(f"\nYour cards: {player_cards}, current score: {calculate(player_cards)}")
    print(f"Computer's cards: [{opponent_card}, {opponent_cards[1:]}], current score: {opponent_score}")

#game functionality 
def blackjack():
    player_cards = [deal_cards(), deal_cards()]
    opponent_cards = [deal_cards()]
    
    display(player_cards, opponent_cards, calculate(player_cards))
    
    #player's turn
    while calculate(player_cards) < 21:
        choice = input("\nType 'y' to get another card or type 'n' to pass: ")
        if choice == 'y':
            player_cards.append(deal_cards())
            display(player_cards, opponent_cards, calculate(player_cards))
        elif choice == 'n':
            break

    player_score = calculate(player_cards)
    if player_score > 21:
        print("\nYou went over... You Lose! 😭")
        return
     
    #opponent's turn
    while calculate(opponent_cards) < 17:
        opponent_cards.append(deal_cards())
        opponent_score = calculate(opponent_cards)
    
    display(player_cards, opponent_cards, player_score, show_opponent_card=True)
    
    if opponent_score > 21 or player_score > opponent_score:
        print("\nYou Win! 😃")

    elif player_score < opponent_score:
        print("\nOpponent Win! 😢")
    
    else:
        print("\nIt's a Draw!")

#print ascii diagram
print_ascii()

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()
