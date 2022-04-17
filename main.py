import random
import time
from Card import Card
from Hand import Hand
from Player import Player


def print_hide_dealer():
    print("\nDealer's Hand:", end="")
    for i in range(0, len(dealer_hand)):
        if i == 1:
            print(' Hidden ', end="")
        else:
            print(" " + dealer_hand[i] + " ", end="")

    for player in players:
        print(f"\n{player.name}'s Hand:", end="")

        for i in range(0, len(player.hand)):
            print(" " + player.hand[i] + " ", end="")
        print('\n')


def print_hands():
    print("Dealer's Hand:", end="")
    for i in range(0, len(dealer.hand)):
        print(" " + dealer_hand[i] + " ", end="")

    for player in players:
        print(f"\n{player.name}'s Hand:", end="")

        for i in range(0, len(player.hand)):
            print(" " + player.hand[i] + " ", end="")
        print('\n')


#def add_up_hand(hand):
    #total_11 = 0
    #total_1 = 0
    #for card_add in hand:
        #if card_add == '♣A' or card_add == '♦A' or card_add == '♥A' or card_add == '♠A':
            #total_1 += 1
            #total_11 += 11
        #elif card_add in ten_value_cards:
            #total_1 += 10
            #total_11 += 10
        #else:
            #total_1 += int(card_add[1])
            #total_11 += int(card_add[1])
    #if total_11 <= 21:
        #print(total_11)
        #return total_11
    #else:
        #print(total_1)
        #return total_1


def transfer_card(hand_1, hand_2, first_idx=None, second_idx=None):
    # Removes the card at first_idx from hand_1, and inserts it at second_idx in hand_2.
    # If no indices are specified, then a random card from hand_1 is removed and appended to the end of hand_2
    if first_idx is None and second_idx is None:
        rand_card = random.randint(0, len(hand_1.cards) - 1)
        hand_2.cards.append(hand_1.cards[rand_card])
        hand_1.cards.pop(rand_card)
    else:
        card_1 = hand_1.cards.pop(first_idx)
        hand_2.cards.insert(second_idx, card_1)


def draw_card(hand):
    rand_card = random.randint(0, len(play_deck.cards) - 1)
    hand.append(play_deck.cards[rand_card])
    play_deck.cards.pop(rand_card)

def main():
    deck_skele = Hand([Card("Ace", "Clubs", [1, 11]), Card("Ace", "Diamonds", [1, 11]),
                       Card("Ace", "Hearts", [1, 11]), Card("Ace", "Spades", [1, 11]),
                       Card("Two", "Clubs", [2]), Card("Ace", "Diamonds", [2]),
                       Card("Ace", "Hearts", [2]), Card("Ace", "Spades", [2]),
                       Card("Three", "Clubs", [3]), Card("Three", "Diamonds", [3]),
                       Card("Three", "Hearts", [3]), Card("Three", "Spades", [3]),
                       Card("Four", "Clubs", [4]), Card("Four", "Diamonds", [4]),
                       Card("Four", "Hearts", [4]), Card("Four", "Spades", [4]),
                       Card("Five", "Clubs", [5]), Card("Five", "Diamonds", [5]),
                       Card("Five", "Hearts", [5]), Card("Five", "Spades", [5]),
                       Card("Six", "Clubs", [6]), Card("Six", "Diamonds", [6]),
                       Card("Six", "Hearts", [6]), Card("Six", "Spades", [6]),
                       Card("Seven", "Clubs", [7]), Card("Seven", "Diamonds", [7]),
                       Card("Seven", "Hearts", [7]), Card("Seven", "Spades", [7]),
                       Card("Eight", "Clubs", [8]), Card("Eight", "Diamonds", [8]),
                       Card("Eight", "Hearts", [8]), Card("Eight", "Spades", [8]),
                       Card("Nine", "Clubs", [9]), Card("Nine", "Diamonds", [9]),
                       Card("Nine", "Hearts", [9]), Card("Nine", "Spades", [9]),
                       Card("Ten", "Clubs", [10]), Card("Ten", "Diamonds", [10]),
                       Card("Ten", "Hearts", [10]), Card("Ten", "Spades", [10]),
                       Card("Jack", "Clubs", [10]), Card("Jack", "Diamonds", [10]),
                       Card("Jack", "Hearts", [10]), Card("Jack", "Spades", [10]),
                       Card("Queen", "Clubs", [10]), Card("Queen", "Diamonds", [10]),
                       Card("Queen", "Hearts", [10]), Card("Queen", "Spades", [10]),
                       Card("King", "Clubs", [10]), Card("King", "Diamonds", [10]),
                       Card("King", "Hearts", [10]), Card("King", "Spades", [10]),
                       ])

    deck_skeleton = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
                     '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
                     '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
                     '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
    ten_value_cards = ['♣10', '♣J', '♣Q', '♣K', '♦10', '♦J', '♦Q', '♦K', '♥10', '♥J', '♥Q', '♥K', '♠10', '♠J', '♠Q', '♠K']

    player_has_bj = False
    dealer_has_bj = False
    game_running = True

    p1_name = input("Enter your name: ")
    print(f"Hi {p1_name}, welcome to Blackjack!")
    players = []
    p1 = Player(p1_name, 1000, Hand(), 0)
    dealer = Player("dealer", 1000, Hand(), 0)
    players.append(p1)

    state = 0
    while game_running:
        while state == 0:  # Betting

            dealer.hand = []
            play_deck = deck_skele

            print(f"You have ${p1.balance} in your balance.")

            p1.bet = int(round(float(input("Enter your bet for the round: "))))
            while (p1.bet % 1) != 0 or p1.bet < 0 or p1.bet > p1.balance:
                print("Sorry, that is not a valid bet.")
                player_bet = int(input("Enter your bet for the round: "))

            state = 1

        while state == 1:  # Dealing
            for i in range(0, 2):
                transfer_card(play_deck.cards, p1.hand)
                transfer_card(play_deck.cards, dealer.hand)

            print(dealer.hand)
            state = 2

        while state == 2:  # Check for natural blackjacks
            dealer.hand.add_up_hand()
            for total in dealer.hand.values:
                if total == 21:
                    dealer_has_bj = True

            if not dealer_has_bj:
                dealer_has_bj = False

            p1.hand.add_up_hand()
            for total in p1.hand.values:
                if total == 21:
                    player_has_bj = True

            if not player_has_bj:
                player_has_bj = False

            if player_has_bj:
                if dealer_has_bj:
                    print_hands()
                    print("Push!\n")
                    state = 0
                    break
                else:
                    print_hands()
                    print(f"Blackjack! {p1_name} wins ${player_bet * 1.5}.\n")
                    p1.balance += (player_bet * 1.5)
                    state = 0
                    break

            if dealer_has_bj:
                print_hands()
                print("Blackjack! Dealer wins.\n")
                p1.balance -= player_bet
                state = 0
                break

            state = 3

    # TODO: Fix state 3 and onward
        while state == 3:  # Player makes play decision
            player_score = add_up_hand(p1.hand)
            print(f"Your total is {player_score}")
            player_decision = \
                (input("Would you like to hit or stand? (Type 'hit' or 'stand' and press enter): ")).lower().strip()

            time.sleep(0.5)

            if player_decision == "hit":
                draw_card(p1.hand)
            print_hide_dealer()
            player_score = add_up_hand(p1.hand)

            if player_score == 21:
                print_hands()
                print(f"Blackjack! {p1_name} wins ${player_bet * 1.5}.\n")
                p1.balance += (player_bet * 1.5)
                state = 0

            elif player_score > 21:
                print(f"Your total is {add_up_hand(p1.hand)}.")
                print(f"Bust! You lose ${player_bet}.\n")
                p1.balance -= player_bet
                state = 0
            else:
                if player_decision == "stand":
                    state = 4
                else:
                    state = 3

        while state == 4:  # Dealer draws cards
            print_hands()
            dealer_score = add_up_hand(dealer_hand)
            state = 5

            while dealer_score < 17:
                draw_card(dealer_hand)
                dealer_score = add_up_hand(dealer_hand)
                print_hands()

                if dealer_score == 21:
                    print_hands()
                    print(f"Dealer Blackjack!")
                    if player_has_bj:
                        print("Push!")
                    else:
                        print(f"You lose ${player_bet}.\n")
                        p1.balance -= (player_bet * 1.5)
                    state = 0
                elif dealer_score > 21:
                    print_hands()
                    print("Dealer Bust!")
                    p1.balance += player_bet
                    state = 0

        while state == 5:  # Showdown
            dealer_score = add_up_hand(dealer_hand)
            if dealer_score > player_score:
                print(f"Dealer wins! You lose {player_bet}\n")
                p1.balance -= player_bet
                state = 0
            elif dealer_score == player_score:
                print("Push!")
                state = 0
            else:
                print(f"You win {player_bet} dollars!\n")
                p1.balance += player_bet
                state = 0

if __name__ == "__main__":
    main()