import random
from collections import deque

from .card import Card


class Deck:
    def __init__(self):
        from Python.packages.cards_game import CARD_COlORS, CARD_RANKS
        self.cards = deque(Card(rank, color) for color in CARD_COlORS for rank in CARD_RANKS)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.popleft() if self.cards else None

    def add_card(self, card):
        from Python.packages.cards_game import DuplicateCard
        if card in self.cards:
            raise DuplicateCard(f'Card {card} is already in deck {self}')
        self.shuffle()

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"{len(self.cards)} cards remainings"