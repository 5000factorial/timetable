from db import Group, Lecturer, Student

def groups():
    return Group.select()

def students():
    return Student.select()

def lecturers():
    return Lecturer.select()