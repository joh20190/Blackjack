class Card:
    def __init__(self, name, suit, values, symbol=None):
        self.name = str(name)
        self.suit = suit
        self.values = values

        if symbol is None:
            if self.name != ("Ace" or "Jack" or "King" or "Queen"):
                self.symbol = str(values[0])
            else:
                self.symbol = self.name[0]
        else:
            self.symbol = symbol

    def __str__(self):
        return_string = ""
        if self.suit == "Hearts":
            return_string += '♥'
        elif self.suit == "Clubs":
            return_string += '♣'
        elif self.suit == "Diamonds":
            return_string += '♦'
        elif self.suit == "Spades":
            return_string += '♠'

        return_string += self.symbol

        return return_string

