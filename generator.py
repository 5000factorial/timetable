from db.group import Group
from db.lecturer import Lecturer
from db.lesson import Lesson
from db.room import Room
from db.student_to_group import StudentToGroup
from db.student import Student
from faker import Faker
import random
from datetime import timedelta, datetime

fake = Faker('ru_RU')


num_of_streams = 3
groups_in_stream = 3
students_in_group = 15

num_of_groups = num_of_streams * groups_in_stream
num_of_students = num_of_groups * students_in_group
num_of_lecturers = 10
num_of_rooms = 15


students = []
for i in range(num_of_students):
    name = fake.name()
    students.append(Student.create(name=name))


lecturers = []
for i in range(num_of_lecturers):
    name = fake.name()
    lecturers.append(Lecturer.create(name=name))


rooms = []
for i in range(num_of_rooms):
    name = str(i+100)
    addres = fake.street_name() + ', ' + fake.building_number()
    rooms.append(Room.create(name=name, address = addres))


groups = []
streams = []
for i in range(num_of_streams):
    stream_name = 'stream' + str(i+1)
    stream = Group.create(name=stream_name)
    streams.append(stream)
    for n in range(groups_in_stream):
        group_name = 'stream' + str(i+1) + 'group' + str(n+1)
        group = Group.create(name=group_name, parentGroupId=stream.id)
        groups.append(group)


#StudentToGroup
for i in range(len(groups)):
    for st in range(students_in_group):
        StudentToGroup.create(GroupID = groups[i].id, StudentID = students[i*students_in_group + st].id) #добавить в группу
        StudentToGroup.create(GroupID = groups[i].parentGroupId, StudentID=students[i * students_in_group + st].id) #добавить в поток


#Lessons
for i in range(1):
    for gr in groups + streams:
        room = random.choice(rooms).id
        lecturer = random.choice(lecturers).id
        title = fake.job()
        time_start = datetime.strptime(fake.time(pattern='%H:%M:%S', end_datetime=None), '%H:%M:%S')
        time_end = time_start + timedelta(minutes=90)
        Lesson.create(group = gr.id, room = room, lecturer = lecturer, name = title, start = time_start, end = time_end)


