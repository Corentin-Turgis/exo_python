from .deck import Card
from .exceptions import CheatException

class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.hand = []

    def add_card_to_hand(self, card: Card):
        if card in self.hand:
            raise CheatException(f'{self.pseudo} is trying to cheat ? {card} is already in is hand')

    def remove_card_from_hand(self, card: Card):
        if card in self.hand:
            self.hand.remove(card)

    def __repr__(self):
        return f"Player({self.pseudo}, Hand: {self.hand})"