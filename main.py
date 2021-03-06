import random
import time
from Card import Card
from Hand import Hand
from Player import Player


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


def print_hands():  # TODO: Finish function
    pass


def print_hide_dealer(): # TODO: Finish function
    pass


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

    players = []
    num_players = int(input("Enter number of players: "))
    idx = num_players
    while idx > 0:
        player_name = input("Enter your name: ")
        print(f"Hi {player_name}, welcome to Blackjack!")
        players.append(Player(player_name, 1000, Hand(), 0, False))
        idx -= 1
    for player in players:
        print(player)
    dealer = Player("Dealer", 1000, Hand(), 0, False)

    game_running = True

    state = 0
    while game_running:
        while state == 0:  # Betting

            play_deck = deck_skele

            for player in players:
                player.bet = 0
                print(f"{player.name}, you have ${player.balance} in your balance.")

                player.bet = int(round(float(input("Enter your bet for the round: "))))
                while (player.bet % 1) != 0 or player.bet < 0 or player.bet > player.balance:
                    print("Sorry, that is not a valid bet.")
                    player_bet = int(input("Enter your bet for the round: "))

            state = 1

        while state == 1:  # Dealing
            dealer.hand = []
            for player in players:
                player.hand = []

            for i in range(0, 2):
                for player in players:
                    transfer_card(play_deck.cards, player.hand)
                transfer_card(play_deck.cards, dealer.hand)

            print_hide_dealer()
            state = 2

        while state == 2:  # Check for natural blackjacks
            for player in players:
                player.has_bj = False
            dealer.has_bj = False

            dealer_score = dealer.hand.update_values()
            if dealer_score == 21:
                dealer.has_bj = True
            else:
                dealer.has_bj = False

            for player in players:
                player_score = player.hand.update_values()
                if player_score == 21:
                    player.has_bj = True
                else:
                    player_has_bj = False

                if player.has_bj:
                    if dealer.has_bj:
                        print_hands()
                        print(f"{player.name} pushes with the dealer.\n")
                else:
                    print_hands()
                    print(f"Blackjack! {player.bet} wins ${player.bet * 1.5}.\n")
                    player.balance += (player.bet * 1.5)

            state = 3

        # TODO: Fix state 3 and onward
        while state == 3:  # Player makes play decision
            for player in players:
                if not player_has_bj:
                    player_decision = ""
                    while player_score < 21 and player_decision != "stand":
                        player_score = player.hand.update_values()
                        print(f"{player.name}, your total is {player_score}")
                        player_decision = \
                            (input(f"{player_name}, would you like to hit or stand?"
                                   f" (Type 'hit' or 'stand' and press enter): ")).lower().strip()

                        time.sleep(0.5)

                        if player_decision == "hit":
                            transfer_card(play_deck, player.hand)
                        print_hide_dealer()
                        player_score = player.hand.update_values()

                        if player_score == 21:
                            print_hands()
                            print(f"Blackjack! {p1_name} wins ${player_bet * 1.5}.\n")
                            p1.balance += (player_bet * 1.5)
                            state = 0

                        elif player_score > 21:
                            print(f"Your total is {p1.hand.update_values()}.")
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
            dealer_score = dealer.hand.update_values()
            state = 5

            while dealer_score < 17:
                transfer_card(play_deck, dealer.hand)
                dealer_score = update_values(dealer_hand)
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
            dealer_score = update_values(dealer_hand)
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
