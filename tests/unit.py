# tests.py
import unittest
from db import Lesson, Lecturer, Room, Group, StudentToGroup, Student
from peewee import SqliteDatabase
import tests.data as data

MODELS = [Lesson, Lecturer, Room, Group, StudentToGroup, Student]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

        # Insert in DB some data to work with
        data.insert()
        q = Lesson.select()
        for i in q:
            print(i.name, i.date)

    def test_foo(self):
        pass

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.

if __name__ == "__main__":
    unittest.main()