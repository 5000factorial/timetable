from flask import Blueprint, send_from_directory, render_template
from os import path
from model.groups import groups, students, lecturers

static = Blueprint('templates',  __name__, template_folder=path.abspath('static'))
print(path.abspath('static'))

@static.route('/')
def index():
    g = list(groups())
    print(g)
    return render_template('index.html', groups=groups(), students=students(), lecturers=lecturers())

@static.route('/lessons/student/<int:student_id>')
def lessons_students(student_id):
    return render_template('lessons/student.html')

@static.route('/lessons/group/<int:group_id>')
def lessons_groups(group_id):
    return render_template('lessons/group.html')

@static.route('/<path:path>')
def etc(path):
    return send_from_directory('static', path)
