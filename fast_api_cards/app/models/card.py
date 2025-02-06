from pydantic import BaseModel

from .enum import Rank, Shape

class Card(BaseModel):
    rank: Rank
    shape: Shape
