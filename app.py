"""
Blackjack Project for 100 Days of Code - Day 11
"""
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []


def first_draw():
    """" draws the first two cards for each player """
    player_hand.clear()
    dealer_hand.clear()
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))


def another_card(hand):
    """ adds another card to the hand """
    hand.append(random.choice(cards))


def score(hand):
    """ calculates the score of the hand. If over 21, will check for aces and score accordingly """
    num_aces = hand.count(11) or 0
    hand.sort()
    if sum(hand) > 21:
        hand_with_aces = hand.copy()
        for ace in range(num_aces):
            hand_with_aces[ace] = 1
            if sum(hand_with_aces) <= 21:
                return sum(hand_with_aces)
    return sum(hand)


def game_over():
    """ checks to see if there is an instant game over (either player over or at 21) """
    if score(player_hand) > 21 or score(dealer_hand) == 21:
        return 'dealer'
    if score(dealer_hand) > 21 or score(player_hand) == 21:
        return 'player'
    return False


def winner_check():
    """ checks for a winner at the end of the game. If no winner, retunrs False """
    if score(player_hand) > 21 and score(dealer_hand) > 21:
        return False
    if game_over():
        return game_over()
    if score(player_hand) > score(dealer_hand):
        return 'player'
    if score(dealer_hand) > score(player_hand):
        return 'dealer'
    return False


def dealer_draws():
    """ dealer draws cards if the hand is under 17 """
    while sum(dealer_hand) < 17:
        print('Dealer must take another card...')
        another_card(dealer_hand)
        print('Dealer hand is: ', dealer_hand, "\n")


def play_blackjack():
    """ starts the game of blackjack! """
    print(logo)
    first_draw()

    print('Your hand: ', player_hand)
    print('Dealer has:', dealer_hand[0])
    print('\n')

    while not game_over():
        hit = input('Would you like another card? (y/N): ')

        if hit == 'y':
            another_card(player_hand)
        else:
            break

        print('Your hand: ', player_hand, "\n")
        if game_over():
            break

    print('Dealer hand is: ', dealer_hand, "\n")
    dealer_draws()

    if winner_check():
        print(f'{winner_check().title()} Wins!')
    else:
        print("It's a DRAW!!!\n")

    print('You: ', score(player_hand), 'Dealer: ', score(dealer_hand))


play_blackjack()

while True:
    keep_playing = input("Would you like to play another game? (Y/n): ")
    if keep_playing != 'n':
        play_blackjack()
    else:
        break

print('Thank you for playing!!!')
