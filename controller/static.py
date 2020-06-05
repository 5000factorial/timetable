from flask import Blueprint, send_from_directory, render_template, request
from os import path
from model.groups import groups, students, lecturers
from db import Group, Lecturer, Student, Room, Lesson
from flask import jsonify
import datetime
from peewee import *


static = Blueprint('templates',  __name__, template_folder=path.abspath('static'))
print(path.abspath('static'))


@static.route('/')
def index():
    g = list(groups())
    print(g)
    return render_template('index.html', groups=groups(), students=students(), lecturers=lecturers())


@static.route('/lessons/student/<int:student_id>')
def lessons_students(student_id):
    return render_template('lessons/student.html', student=Student.get_by_id(student_id))


@static.route('/lessons/group/<int:group_id>')
def lessons_groups(group_id):
    return render_template('lessons/group.html', group=Group.get_by_id(group_id))


@static.route('/lessons/lecturer/<int:lecturer_id>')
def lessons_lecturers(lecturer_id):
    return render_template('lessons/lecturer.html', lecturer=Lecturer.get_by_id(lecturer_id))


@static.route('/lessons/new/')
def new_lesson():
    return render_template(
        'lessons/new.html',
        groups=Group.select(),
        lecturers=Lecturer.select(),
        addresses=Room.select(Room.address).group_by(Room.address)
    )

@static.route('/api/rooms/address/', methods=['OPTIONS'])
def rooms_by_address():
    print(request.form)
    if not 'start' in request.form.keys():
        return jsonify(
            [
                {'id': i.id, 'name': i.name} 
                for i in Room.select().where(
                    Room.address == request.form['address']
                )
            ])
    else:
        data = dict(request.form)
        print('awdawdawdaw')
        start = data['start'].split(':')
        data['start'] = datetime.datetime.now().replace(hour=int(start[0]), minute=int(start[1]), second=0)
        data['end'] = data['start'] + datetime.timedelta(hours=1, minutes=30)
        data['start'] = datetime.time(hour=data['start'].hour, minute=data['start'].minute)
        data['end'] = datetime.time(hour=data['end'].hour, minute=data['end'].minute)
        data['date'] = datetime.datetime.fromisoformat(data['date'].replace('Z', '')).date()
        qq = Room.select().where((Room.address == data['address']) & Room.id.not_in(
            Room.select(Room.id).join(Lesson).where(
                (Lesson.date == data['date']) &
                (
                    ((data['start'] >= Lesson.start) & (data['start'] <= Lesson.end))
                    | ((data['end'] >= Lesson.start) & (  data['end'] <= Lesson.end))
                )
            )
        ))
        print(list(qq))
        return jsonify([{'id': i.id, 'name': i.name} for i in qq])


@static.route('/<path:path>')
def etc(path):
    return send_from_directory('static', path)
