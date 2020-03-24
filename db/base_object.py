from peewee import * # pylint: disable=unused-wildcard-import
from .connector import db

class BaseClass(Model):
    class Meta:
        database = db