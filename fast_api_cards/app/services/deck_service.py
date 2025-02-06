import random

from fast_api_cards.app.models import Deck, Rank, Shape, Card
from typing import List

def create_shuffled_deck() -> Deck:
    """
    Crée un deck de 52 cartes et le mélange.
    """
    cards = [
        Card(rank=r, shape=s)  # r est un Rank, s un Suit
        for s in Shape
        for r in Rank
    ]
    random.shuffle(cards)
    return Deck(cards=cards)

def deal_deck(deck: Deck, nb_parts: int) -> List[List[Card]]:
    """
    Distribue toutes les cartes de `deck` en nb_parts mains,
    de manière round-robin.
    """
    if nb_parts <= 0 or nb_parts > len(deck.cards):
        raise ValueError("nb_parts doit être >= 1")

    hands = [[] for _ in range(nb_parts)]
    i = 0
    for card in deck.cards:
        hands[i % nb_parts].append(card)
        i += 1

    return hands
