from peewee import JOIN
from db import Lesson, Group, StudentToGroup, Room, Lecturer, Student
from playhouse.shortcuts import model_to_dict
from flask import jsonify

# TODO: maybe run some perfomance tests

def query_to_json_mapper(query):
    return jsonify([
        {
            'name': i.name,
            'start': i.start.isoformat(),
            'end': i.end.isoformat(),
            'date': i.date.isoformat(),
            'room': i.room.name,
            'address': i.room.address,
            'group': i.group.name
        } 
        for i in query
    ])

def for_student(student_id):
    query = (Lesson
        .select(Lesson.name, Lesson.start, Lesson.end, Lesson.date, Room.name, Room.address, Group.name)
        .join(Group)
        .join(StudentToGroup)
        .join(Student)
        .switch(Lesson)
        .join(Room)
        .switch(Lesson)
        .where(Student.id == student_id)
    )
    return query_to_json_mapper(query)

def for_group(group_id, date_frame=(None, None)):
    query = (Lesson
        .select(Lesson.name, Lesson.start, Lesson.end, Lesson.date, Room.name, Room.address, Group.name)
        .join(Group).switch(Lesson)
        .join(Lecturer, JOIN.LEFT_OUTER).switch(Lesson).
        join(Room, JOIN.LEFT_OUTER).switch(Lesson).
        where(Lesson.group == group_id)
    )
    return query_to_json_mapper(query)