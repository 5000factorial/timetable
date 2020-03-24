from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

class Room(BaseClass):
    id = BigAutoField(
        null = False,
        primary_key = True
    )
    name = CharField()
    address = CharField()

Room.create_table()
