from db import Lesson, Group, StudentToGroup, Room, Lecturer, Student

def groups():
    return Group.select()

def students():
    return Student.select()

def lecturers():
    return Lecturer.select()