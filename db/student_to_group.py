from peewee import * # pylint: disable=unused-wildcard-import
from db.base_object import BaseClass

from db.student import Student
from db.group import Group

class StudentToGroup(BaseClass):
    StudentID = ForeignKeyField(Student)
    GroupID = ForeignKeyField(Group)

StudentToGroup.create_table()