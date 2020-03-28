from flask import Blueprint, request
from flasgger import swag_from
import model.lessons
from model.exceptions import NoSuchDBRecordException

lessons = Blueprint('lessons',  __name__, url_prefix='/api/lessons')

@lessons.route('/student/<int:student_id>')
@swag_from('swagger/lessons_student.yml')
def get_lessons_for_student(student_id):
    # TODO: request.args.get('date-from'), request.args.get('date-to')
    try:
        return model.lessons.for_student(student_id)
    except NoSuchDBRecordException:
        return 'Not Found', 404

@lessons.route('/group/<int:group_id>')
@swag_from('swagger/lessons_group.yml')
def get_lessons_for_group(group_id):
    try:
        return model.lessons.for_group(group_id)
    except NoSuchDBRecordException:
        return 'Not Found', 404