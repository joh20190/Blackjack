import random
import time


def print_hide_dealer():
    print("\nDealer's Hand:", end="")
    for i in range(0, len(dealer_hand)):
        if i == 1:
            print(' Hidden ', end="")
        else:
            print(" " + dealer_hand[i] + " ", end="")

    print(f"\n{player_name}'s Hand:", end="")
    for i in range(0, len(player_hand)):
        print(" " + player_hand[i] + " ", end="")
    print('\n')


def print_hands():
    print("Dealer's Hand:", end="")
    for i in range(0, len(dealer_hand)):
        print(" " + dealer_hand[i] + " ", end="")

    print(f"\n{player_name}'s Hand:", end="")
    for i in range(0, len(player_hand)):
        print(" " + player_hand[i] + " ", end="")
    print('\n')


def add_up_hand(hand):
    total_11 = 0
    total_1 = 0
    for card_add in hand:
        if card_add == '♣A' or card_add == '♦A' or card_add == '♥A' or card_add == '♠A':
            total_1 += 1
            total_11 += 11
        elif card_add in ten_value_cards:
            total_1 += 10
            total_11 += 10
        else:
            total_1 += int(card_add[1])
            total_11 += int(card_add[1])
    if total_11 <= 21:
        print(total_11)
        return total_11
    else:
        print(total_1)
        return total_1


def draw_card(hand):
    rand_card = random.randint(0, len(play_deck) - 1)
    hand.append(play_deck[rand_card])
    play_deck.pop(rand_card)


state = 0
deck_skeleton = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
                 '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
                 '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
                 '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
ten_value_cards = ['♣10', '♣J', '♣Q', '♣K', '♦10', '♦J', '♦Q', '♦K', '♥10', '♥J', '♥Q', '♥K', '♠10', '♠J', '♠Q', '♠K']

player_balance = 1000
player_has_bj = False
dealer_has_bj = False
play_deck = []
player_hand = []
dealer_hand = []
game_running = True

player_name = input("Enter your name: ")
print(f"Hi {player_name}, welcome to Blackjack!")

while game_running:
    while state == 0:  # Betting
        player_hand = []
        dealer_hand = []
        play_deck = deck_skeleton.copy()

        print(f"You have ${player_balance} in your balance.")

        player_bet = int(round(float(input("Enter your bet for the round: "))))
        while (player_bet % 1) != 0 or player_bet < 0 or player_bet > player_balance:
            print("Sorry, that is not a valid bet.")
            player_bet = int(input("Enter your bet for the round: "))

        state = 1

    while state == 1:  # Dealing
        for i in range(0, 2):
            draw_card(player_hand)
            draw_card(dealer_hand)

        print_hide_dealer()
        state = 2

    while state == 2:  # Check for natural blackjacks
        if add_up_hand(dealer_hand) == 21:
            dealer_has_bj = True
        else:
            dealer_has_bj = False

        if add_up_hand(player_hand) == 21:
            player_has_bj = True
        else:
            player_has_bj = False

        if player_has_bj:
            if dealer_has_bj:
                print_hands()
                print("Push!\n")
                state = 0
                break
            else:
                print_hands()
                print(f"Blackjack! {player_name} wins ${player_bet * 1.5}.\n")
                player_balance += (player_bet * 1.5)
                state = 0
                break

        if dealer_has_bj:
            print_hands()
            print("Blackjack! Dealer wins.\n")
            player_balance -= player_bet
            state = 0
            break

        state = 3

    while state == 3:  # Player makes play decision
        player_score = add_up_hand(player_hand)
        print(f"Your total is {player_score}")
        player_decision = \
            (input("Would you like to hit or stand? (Type 'hit' or 'stand' and press enter): ")).lower().strip()

        time.sleep(0.5)

        if player_decision == "hit":
            draw_card(player_hand)
        print_hide_dealer()
        player_score = add_up_hand(player_hand)

        if player_score == 21:
            print_hands()
            print(f"Blackjack! {player_name} wins ${player_bet * 1.5}.\n")
            player_balance += (player_bet * 1.5)
            state = 0

        elif player_score > 21:
            print(f"Your total is {add_up_hand(player_hand)}.")
            print(f"Bust! You lose ${player_bet}.\n")
            player_balance -= player_bet
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
                    player_balance -= (player_bet * 1.5)
                state = 0
            elif dealer_score > 21:
                print_hands()
                print("Dealer Bust!")
                player_balance += player_bet
                state = 0

    while state == 5:  # Showdown
        dealer_score = add_up_hand(dealer_hand)
        if dealer_score > player_score:
            print(f"Dealer wins! You lose {player_bet}\n")
            player_balance -= player_bet
            state = 0
        elif dealer_score == player_socre:
            print("Push!")
            state = 0
        else:
            print(f"You win {player_bet} dollars!\n")
            player_balance += player_bet
            state = 0
