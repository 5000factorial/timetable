from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

from db.group import Group
from db.room import Room
from db.lecturer import Lecturer

class Lesson(BaseClass):
    id = BigAutoField(
        null = False,
        primary_key = True
    )
    group = ForeignKeyField(Group)
    room = ForeignKeyField(Room)
    lecturer = ForeignKeyField(Lecturer)
    name = CharField()
    start = TimeField()
    end = TimeField()

Lesson.create_table()
