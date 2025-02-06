from fastapi import APIRouter, HTTPException
from typing import List
from fast_api_cards.app.services import create_shuffled_deck, deal_deck
from fast_api_cards.app.models import Deck, Card

deck_router = APIRouter()

@deck_router.get("/shuffled", response_model=Deck)
def get_shuffled_deck() -> Deck:
    """
    Retourne un deck de 52 cartes déjà mélangé.
    """
    return create_shuffled_deck()

@deck_router.get("/deal/{nb_parts}", response_model=List[List[Card]])
def get_deal(nb_parts: int = 4):
    """
    Distribue un deck de 52 cartes en `nb_parts` mains (4 par défaut).
    """
    deck = create_shuffled_deck()
    try:
        return deal_deck(deck, nb_parts)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
