import random


class Hand:
    def update_values(self):
        for card in self.cards:
            for idx, value in enumerate(card.values):
                try:
                    self.values[idx] += value
                except IndexError:
                    self.values.append(0)
                    self.values[idx] += value

        self.values.sort()
        maximum = 0
        for score in self.values:
            if score > maximum >= 21:
                maximum = score

        return maximum

    def get_score(self):
        pass
        # TODO finish function

    def __init__(self, cards=None, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
        # Hands can have different values because cards can have different values i.e. an ace in Blackjack can be
        # a 1 or an 11. The values list is sorted from the least value to the greatest value.

    def __str__(self):
        return_string = ""
        for card in self.cards:
            return_string += card.__str__() + " "

        return return_string
