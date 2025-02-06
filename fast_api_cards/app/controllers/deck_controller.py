from typing import List

from fastapi import APIRouter, HTTPException

from fast_api_cards.app.models.card_model import CardModel
from fast_api_cards.app.models.deck_model import DeckModel
from fast_api_cards.app.services.deck_service import create_shuffled_deck, deal_deck

deck_controller = APIRouter()


@deck_controller.get("/deck/shuffled", response_model=DeckModel)
def get_shuffled_deck() -> DeckModel:
    """
    Retourne un deck de 52 cartes déjà mélangé.
    """
    return create_shuffled_deck()

# return une hand en vrais mais on fera ca mieux sur le projet
@deck_controller.get("/deck/deal/{nb_part}", response_model=List[List[CardModel]])
def deal_cards(nb_part: int = 4):
    """
    Exemple: distribuer un deck en 4 mains (paramètre nb_part).
    """
    deck = create_shuffled_deck()
    if 0 < nb_part <= len(deck.cards):
        parts = deal_deck(deck, nb_part)
        return parts
    raise HTTPException(status_code=422, detail='Unprocessable Entity')