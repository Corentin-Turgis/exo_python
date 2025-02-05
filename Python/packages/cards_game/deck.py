import random
from collections import namedtuple, deque
from Python.packages.cards_game import CARD_COlORS, CARD_RANKS, DuplicateCard

Card = namedtuple('Card', ['rank', 'color'])

class Deck:
    def __init__(self):
        self.cards = deque(Card(rank, color) for color in CARD_COlORS for rank in CARD_RANKS)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.popleft() if self.cards else None

    def add_card(self, card):
        if card in self.cards:
            raise DuplicateCard(f'Card {card} is already in deck {self}')

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({len(self.cards)} cards remainings"