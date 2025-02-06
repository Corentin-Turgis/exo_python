import random
from ..models.card_model import CardModel
from ..models.deck_model import DeckModel

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SHAPES = ["heart", "diamond", "club", "spade"]

def create_shuffled_deck() -> DeckModel:
    cards = []
    for shape in SHAPES:
        for rank in RANKS:
            cards.append(CardModel(rank=rank, shape=shape))

    random.shuffle(cards)

    return DeckModel(cards=cards)

def deal_deck(deck: DeckModel, nb_part: int) -> list[list[CardModel]]:
    """
    Distribue toutes les cartes de 'deck' (round-robin).
    Retourne une mains.
    """
    if nb_part <= 0:
        raise ValueError("Le nombre de parts doit être > 0")

    cards = deck.cards[:]  # copie
    parts = [[] for _ in range(nb_part)]
    i = 0

    while cards:
        # On pioche la "dernière" plus performant
        card = cards.pop()
        parts[i % nb_part].append(card)
        i += 1

    # "première" carte -> pop(0)
    # moins performant
    return parts
