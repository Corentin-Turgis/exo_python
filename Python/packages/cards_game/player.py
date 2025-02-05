import string

from .deck import Card
from .exceptions import CheatException, RemoveException

class Player:
    def __init__(self, pseudo):
        self.pseudo: string = pseudo
        self.hand = set()

    def add_card_to_hand(self, card: Card):
        if card in self.hand:
            raise CheatException(f'{self.pseudo} is trying to cheat ? {card} is already in is hand')
        self.hand.add(card)
        print(f'{self.pseudo} draw a {card}')

    def remove_card_from_hand(self, card: Card):
        if card not in self.hand:
            raise RemoveException(f"{card} isn't in {self}")
        self.hand.remove(card)
        print(f'{self.pseudo} discard {card}')

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.pseudo == other.pseudo
        return False

    def __str__(self):
        return self.pseudo

    def __repr__(self):
        return f"Player({self.pseudo}, Hand: {self.hand})"