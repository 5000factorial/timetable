from flask import Blueprint, request
from flasgger import swag_from
import model.lessons
from model.exceptions import NoSuchDBRecordException
import datetime

lessons = Blueprint('lessons',  __name__, url_prefix='/api/lessons')


@lessons.route('/student/<int:student_id>')
@swag_from('swagger/lessons_student.yml')
def get_lessons_for_student(student_id):
    date_from = request.args.get('date-from')
    date_to = request.args.get('date-to')
    try:
        return model.lessons.for_student(student_id, date_from, date_to)
    except NoSuchDBRecordException:
        return 'Not Found', 404


@lessons.route('/group/<int:group_id>')
@swag_from('swagger/lessons_group.yml')
def get_lessons_for_group(group_id):
    date_from = request.args.get('date-from')
    date_to = request.args.get('date-to')
    try:
        return model.lessons.for_group(group_id, date_from, date_to)
    except NoSuchDBRecordException:
        return 'Not Found', 404


@lessons.route('/lecturer/<int:lecturer_id>')
@swag_from('swagger/lessons_lecturer.yml')
def get_lessons_for_lecturer(lecturer_id):
    date_from = request.args.get('date-from')
    date_to = request.args.get('date-to')
    try:
        return model.lessons.for_lecturer(lecturer_id, date_from, date_to)
    except NoSuchDBRecordException:
        return 'Not Found', 404


@lessons.route('/', methods=['POST'])
def new_lesson():
    data = dict(request.form)
    start = data['start'].split(':')
    data['start'] = datetime.datetime.now().replace(hour=int(start[0]), minute=int(start[1]), second=0)
    data['end'] = data['start'] + datetime.timedelta(hours=1, minutes=30)
    data['start'] = datetime.time(hour=data['start'].hour, minute=data['start'].minute)
    data['end'] = datetime.time(hour=data['end'].hour, minute=data['end'].minute)
    data['date'] = datetime.datetime.fromisoformat(data['date'].replace('Z', '')).date()
    print(data['date'])
    model.lessons.create(data)
    return 'OK', 200