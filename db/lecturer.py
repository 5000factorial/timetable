from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

class Lecturer(BaseClass):
    id = BigAutoField(
        null = False,
        primary_key = True
    )
    name = CharField()

Lecturer.create_table()
