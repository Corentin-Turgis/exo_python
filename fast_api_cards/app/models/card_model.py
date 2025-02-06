from pydantic import BaseModel

class CardModel(BaseModel):
    rank: str
    shape: str
