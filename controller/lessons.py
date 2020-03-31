from flask import Blueprint, request
from flasgger import swag_from
import model.lessons
from model.exceptions import NoSuchDBRecordException

lessons = Blueprint('lessons',  __name__, url_prefix='/api/lessons')

@lessons.route('/student/<int:student_id>')
@swag_from('swagger/lessons_student.yml')
def get_lessons_for_student(student_id):
    date_from = request.args.get('date-from')
    date_to = request.args.get('date-to')
    print(date_from, date_to)
    print([i for i in request.args.items()])
    try:
        return model.lessons.for_student(student_id, date_from, date_to)
    except NoSuchDBRecordException:
        return 'Not Found', 404

@lessons.route('/group/<int:group_id>')
@swag_from('swagger/lessons_group.yml')
def get_lessons_for_group(group_id):
    date_from = request.args.get('date-from')
    date_to = request.args.get('date-to')
    print(date_from, date_to)
    print([i for i in request.args.items()])
    try:
        return model.lessons.for_group(group_id, date_from, date_to)
    except NoSuchDBRecordException:
        return 'Not Found', 404