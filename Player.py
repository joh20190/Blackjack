class Player:
    def __init__(self, name, balance, hand, bet, has_bj):
        self.name = name
        self.balance = balance
        self.hand = hand
        self.bet = bet
        self.has_bj = True

    def __str__(self):
        return f"{self.name}, ${self.balance}"
