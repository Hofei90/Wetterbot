from peewee import *

database = SqliteDatabase('wetterbot.sqlite', **{})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Benachrichtigung(BaseModel):
    inhalt = TextField(null=True)
    next = TextField(null=True)
    typ = TextField(null=True)
    uhrzeit = TextField(null=True)
    userid = IntegerField(null=True)

    class Meta:
        table_name = 'benachrichtigung'


class User(BaseModel):
    nachname = TextField(null=True)
    userid = AutoField(null=True)
    username = TextField(null=True)
    vorname = TextField(null=True)

    class Meta:
        table_name = 'user'
