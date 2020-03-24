from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

class Group(BaseClass):
    id = BigAutoField(
        null = False,
        primary_key = True
    )
    name = CharField()
    parentGroupId = BigIntegerField(
        null=True
    )

Group.create_table()
