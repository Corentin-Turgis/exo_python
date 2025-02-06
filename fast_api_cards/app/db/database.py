from peewee import SqliteDatabase

DATABASE_URL = "fastapi_deck.db"

db = SqliteDatabase(
    DATABASE_URL,
)
