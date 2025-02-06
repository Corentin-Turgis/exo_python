from peewee import Model, CharField, AutoField
from .database import db

class BaseORM(Model):
    class Meta:
        database = db

class CardORM(BaseORM):
    id = AutoField()
    rank = CharField()
    shape = CharField()
