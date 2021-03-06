from peewee import JOIN
from db import Lesson, Group, StudentToGroup, Room, Lecturer, Student
from playhouse.shortcuts import model_to_dict
from flask import jsonify
from model.exceptions import NoSuchDBRecordException
from datetime import date

# TODO: maybe run some perfomance tests


def query_to_json_mapper(query):
    try:
        ret = jsonify([
            {
                'name': i.name,
                'start': i.start,
                'end': i.end,
                'date': i.date.isoformat(),
                'room': i.room.name,
                'address': i.room.address,
                'group': i.group.name
            } 
            for i in query
        ])
    except Exception:
        ret = jsonify([
            {
                'name': i.name,
                'start': i.start.isoformat(),
                'end': i.end.isoformat(),
                'date': i.date,
                'room': i.room.name,
                'address': i.room.address,
                'group': i.group.name
            } 
            for i in query
        ])
    return ret


def for_student(student_id, date_from = None, date_to = None):
    """
    Retrives lessons for student filtered by date

    Keyword arguments:
    student_id - int ID of a student
    date_from - date in iso format string (!) or None (default: None)
    date_to - date in iso format string (!) or None (default: None)
    """
    # Check if student exists
    try:
        Student.get_by_id(student_id)
    except Student.DoesNotExist:
        raise NoSuchDBRecordException("Student with id {} does not exist in database".format(student_id))
    
    query = (Lesson
        .select(Lesson.name, Lesson.start, Lesson.end, Lesson.date, Room.name, Room.address, Group.name)
        .join(Group)
        .join(StudentToGroup)
        .join(Student)
        .switch(Lesson)
        .join(Room)
        .switch(Lesson)
        .where(Student.id == student_id)
        .order_by(Lesson.date, Lesson.start)
    )
    if date_from != None:
        query = query.where(Lesson.date > date.fromisoformat(date_from))
    if date_to != None:
        query = query.where(Lesson.date < date.fromisoformat(date_to))
    return query_to_json_mapper(query)


def for_group(group_id, date_from = None, date_to = None):
    """
        Retrives lessons for group filtered by date

        Keyword arguments:
        group_id - int ID of a group
        date_from - date in iso format string (!) or None (default: None)
        date_to - date in iso format string (!) or None (default: None)
        """
    # Check if group exists
    try:
        Group.get_by_id(group_id)
    except Group.DoesNotExist:
        raise NoSuchDBRecordException("Group with id {} does not exist in database".format(group_id))

    query = (Lesson
             .select(Lesson.name, Lesson.start, Lesson.end, Lesson.date, Room.name, Room.address, Group.name)
             .join(Group).switch(Lesson)
             .join(Lecturer).switch(Lesson)
             .join(Room).switch(Lesson)
             .where(Lesson.group == group_id)
             .order_by(Lesson.date, Lesson.start)
             )
    if date_from != None:
        query = query.where(Lesson.date > date.fromisoformat(date_from))
    if date_to != None:
        query = query.where(Lesson.date < date.fromisoformat(date_to))
    return query_to_json_mapper(query)


def for_lecturer(lecturer_id, date_from = None, date_to = None):
    """
        Retrives lessons for lecturer filtered by date

        Keyword arguments:
        lecturer_id - int ID of a lecturer
        date_from - date in iso format string (!) or None (default: None)
        date_to - date in iso format string (!) or None (default: None)
        """
    # Check if group exists
    try:
        Lecturer.get_by_id(lecturer_id)
    except Lecturer.DoesNotExist:
        raise NoSuchDBRecordException("Lecturer with id {} does not exist in database".format(lecturer_id))

    query = (Lesson
             .select(Lesson.name, Lesson.start, Lesson.end, Lesson.date, Room.name, Room.address, Group.name)
             .join(Group).switch(Lesson)
             .join(Lecturer).switch(Lesson)
             .join(Room).switch(Lesson)
             .where(Lesson.lecturer == lecturer_id)
             .order_by(Lesson.date, Lesson.start)
             )
    if date_from != None:
        query = query.where(Lesson.date > date.fromisoformat(date_from))
    if date_to != None:
        query = query.where(Lesson.date < date.fromisoformat(date_to))
    return query_to_json_mapper(query)


def create(data, fail_silently=False):
    students_affected = (
        Student.select(Student.id)
        .join(StudentToGroup)
        .join(Group)
        .where(Group.id == data['group'])
    )
    count_conflict_lessons = (
        Lesson.select()
        .join(Room).switch(Lesson)
        .join(Lecturer).switch(Lesson)
        .join(Group).join(StudentToGroup).join(Student).switch(Lesson)
        .where(
            (Lesson.date == data['date'])
            & (
                (data['start'] >= Lesson.start) & (data['start'] <= Lesson.end)
                | (data['end'] >= Lesson.start) & (  data['end'] <= Lesson.end)
            )
            & (
                (Lesson.room == data['room'])
                | (Lesson.lecturer == data['lecturer'])
                | (Lesson.group == data['group'])
            )
        )
        .group_by(Lesson)
        .count()
    )
    if (count_conflict_lessons == 0):
        l = Lesson(**data)
        l.save()
    elif not fail_silently:
        raise Exception(f'Lessons conflicting: {count_conflict_lessons}')
