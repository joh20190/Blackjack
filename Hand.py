import random


class Hand:
    def add_up_hand(self):
        for card in self.cards:
            for idx, value in enumerate(card.values):
                self.values[idx] += value

        self.values.sort()

    def __init__(self, cards, values=None):
        self.cards = cards
        # Hands can have different values because cards can have different values i.e. an ace in Blackjack can be
        # a 1 or an 11. The values list is sorted from the least value to the greatest value.

    def print(self):
        for card in self.cards:
            print(card.values, end=" ")
        print()
