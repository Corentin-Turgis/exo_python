from fastapi import APIRouter, HTTPException
from typing import List

from pydantic import BaseModel

from fast_api_cards.app.db.models_pewee import CardORM
from fast_api_cards.app.models import Card  # Pydantic

card_router = APIRouter()


class CardCreate(BaseModel):
    rank: str
    shape: str


@card_router.get("/", response_model=List[Card])
def list_cards():
    query = CardORM.select()
    result = [Card(rank=row.rank, shape=row.shape) for row in query]
    return result


@card_router.post("/", response_model=Card)
def create_card(card_in: CardCreate):
    new_card = CardORM.create(
        rank=card_in.rank,
        shape=card_in.shape
    )
    return Card(rank=new_card.rank, shape=new_card.shape)


@card_router.delete("/{card_id}")
def delete_card(card_id: int):
    row_deleted = CardORM.delete_by_id(card_id)
    if not row_deleted:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"detail": "Card deleted"}
