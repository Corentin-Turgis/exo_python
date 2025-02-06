from fastapi import FastAPI

from fast_api_cards.app.controllers import deck_controller


def create_app() -> FastAPI:
    api = FastAPI(title="Card API")
    api.include_router(deck_controller, prefix="", tags=["Deck"])
    return api

app = create_app()
