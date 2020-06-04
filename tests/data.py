from db import Lesson, Lecturer, Room, Group, StudentToGroup, Student
from datetime import date, time

def insert():
    rooms = [
        {'name':'1','address':'address1', 'id':1},
        {'name':'10','address':'address1', 'id':2},
        {'name':'20','address':'address1', 'id':3},
        {'name':'30','address':'address1', 'id':4},
        {'name':'40','address':'address1', 'id':5},
        {'name':'1','address':'address2', 'id':6},
        {'name':'5','address':'address2', 'id':7},
        {'name':'10','address':'address2', 'id':8},
        {'name':'15','address':'address2', 'id':9},
        {'name':'20','address':'address2', 'id':10}
    ]

    Room.insert_many(rooms).execute()

    lecturers = [
        {'name':'Lecturer One'},
        {'name':'Lecturer One'},
        {'name':'Lecturer Two'},
        {'name':'Lecturer Three'},
        {'name':'Lecturer Four'}
    ]

    Lecturer.insert_many(lecturers).execute()

    groups = [
        {'name':'stream1', 'id': 1},
        {'name':'stream2', 'id': 2},
        {'name':'group1', 'parentGroupId':1, 'id': 3},
        {'name':'group2', 'parentGroupId':1, 'id': 4},
        {'name':'group3', 'parentGroupId':2, 'id': 5},
        {'name':'group4', 'parentGroupId':2, 'id': 6},
        {'name': 'group5', 'id': 7}
    ]

    Group.insert_many(groups).execute()

    students = [{'id': i, 'name': 'student ' + str(i)} for i in range(1,41)]

    Student.insert_many(students).execute()

    stg = [{'StudentID':i, 'GroupID':1} for i in range(1,21)]
    stg += [{'StudentID':i, 'GroupID':2} for i in range(21,41)]
    stg += [{'StudentID':i, 'GroupID':3} for i in range(1,11)]
    stg += [{'StudentID':i, 'GroupID':4} for i in range(11,21)]
    stg += [{'StudentID':i, 'GroupID':5} for i in range(21,31)]
    stg += [{'StudentID':i, 'GroupID':6} for i in range(31,41)]
    stg += [{'StudentID':i, 'GroupID':7} for i in range(1,41,5)]

    StudentToGroup.insert_many(stg).execute()

    dates = [date(2020,2,10), date(2020,2,11), date(2020,2,12), date(2020,2,13)]
    times = [(time(9,30), time(11,5)), (time(11,15), time(12,50)), (time(13,40), time(15,15))]
    lessons = []

    for d in dates:
        (s,e) = times[0]
        #print(e)
        lessons.append({'group': 1, 'room': 1, 'lecturer': 1, 'name': 'Lecture', 'start': s, 'end': e, 'date': d})
        lessons.append({'group': 2, 'room': 2, 'lecturer': 2, 'name': 'Lecture', 'start': s, 'end': e, 'date': d})
        (s,e) = times[1]
        lessons.append({'group': 3, 'room': 3, 'lecturer': 3, 'name': 'Practice', 'start': s, 'end': e, 'date': d})
        lessons.append({'group': 4, 'room': 4, 'lecturer': 4, 'name': 'Practice', 'start': s, 'end': e, 'date': d})
        lessons.append({'group': 5, 'room': 1, 'lecturer': 1, 'name': 'Practice', 'start': s, 'end': e, 'date': d})
        lessons.append({'group': 6, 'room': 2, 'lecturer': 2, 'name': 'Practice', 'start': s, 'end': e, 'date': d})
        (s,e) = times[2]
        lessons.append({'group': 7, 'room': 3, 'lecturer': 3, 'name': 'Elective', 'start': s, 'end': e, 'date': d})

    print(lessons)
    Lesson.insert_many(lessons).execute()