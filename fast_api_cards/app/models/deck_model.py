from pydantic import BaseModel
from typing import List
from .card_model import CardModel

class DeckModel(BaseModel):
    cards: List[CardModel]
