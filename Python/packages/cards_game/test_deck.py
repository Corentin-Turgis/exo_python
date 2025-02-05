import random

from Python.packages.cards_game import Deck


def test_shuffle_changes_order():
    deck = Deck()
    original_order = list(deck.cards)

    deck.shuffle()
    shuffled_order = list(deck.cards)

    assert len(original_order) == len(shuffled_order), "Le deck a perdu ou ajouté des cartes"

    if original_order == shuffled_order:
        deck.shuffle() ## On sait jamais !
        shuffled_order = list(deck.cards)
        assert original_order != shuffled_order, "Le shuffle n'a pas modifié l'ordre après 2 tentatives"

def test_shuffle_preserves_all_cards():
    deck = Deck()
    original_cards = set(deck.cards)

    deck.shuffle()
    shuffled_cards = set(deck.cards)

    assert original_cards == shuffled_cards, "Le shuffle a modifié ou perdu des cartes"

def test_shuffle_randomness():
    deck = Deck()
    deck.shuffle()
    order1 = list(deck.cards)

    deck.shuffle()
    order2 = list(deck.cards)

    assert order1 != order2, "Deux shuffles successifs donnent le même ordre, ce qui est peu probable"

def test_shuffle_with_fixed_seed():
    deck1 = Deck()
    deck2 = Deck()

    random.seed(31)
    deck1.shuffle()
    order1 = list(deck1.cards)

    random.seed(31)
    deck2.shuffle()
    order2 = list(deck2.cards)

    assert order1 == order2, "Avec un seed fixé, les shuffles doivent être identiques et en faite non les deques n'ont pas le meme comportement que les listes quand on shuffle"
