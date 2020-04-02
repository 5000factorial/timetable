from flask import Blueprint, send_from_directory
from os import path

static = Blueprint('templates',  __name__, static_folder=path.abspath('static'))
print(path.abspath('static'))


@static.route('/')
def index():
    return static.send_static_file('index.html')


@static.route('/lessons/student/<int:student_id>')
def lessons_students(student_id):
    return static.send_static_file('lessons/student.html')


@static.route('/lessons/group/<int:group_id>')
def lessons_groups(group_id):
    return static.send_static_file('lessons/group.html')


@static.route('/lessons/lecturer/<int:lecturer_id>')
def lessons_lecturers(lecturer_id):
    return static.send_static_file('lessons/lecturer.html')


@static.route('/<path:path>')
def etc(path):
    return send_from_directory('static', path)
