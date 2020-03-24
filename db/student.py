from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

class Student(BaseClass):
    id = BigAutoField(
        null = False,
        primary_key = True
    )
    name = CharField()

Student.create_table()