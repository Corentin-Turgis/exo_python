from Python.packages.cards_game import CheatException


class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.hand = []

    def add_card_to_hand(self, card):
        if card in self.hand:
            raise CheatException(f'{self.pseudo} is trying to cheat ? {card} is already in is hand')

    def __repr__(self):
        return f"Player({self.pseudo}, Hand: {self.hand})"