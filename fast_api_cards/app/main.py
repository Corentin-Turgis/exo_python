from fastapi import FastAPI
from contextlib import asynccontextmanager

from fast_api_cards.app.api import deck_router
from fast_api_cards.app.db.database import db
from fast_api_cards.app.db.models_pewee import CardORM

@asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([CardORM])

    yield  # => l'app tourne

    if not db.is_closed():
        db.close()

def create_application() -> FastAPI:
    app = FastAPI(title="Deck API", version="1.0.0", lifespan=lifespan)
    # On inclut les routers
    app.include_router(deck_router, prefix="/deck", tags=["deck"])
    return app

app = create_application()
