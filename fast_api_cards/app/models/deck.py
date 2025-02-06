from typing import List
from pydantic import BaseModel
from .card import Card

class Deck(BaseModel):
    cards: List[Card]
