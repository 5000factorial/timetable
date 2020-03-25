from flask import Blueprint, request
from flasgger import swag_from
import model.lessons

lessons = Blueprint('lessons',  __name__, url_prefix='/lessons')

@lessons.route('/student/<int:student_id>')
@swag_from('swagger/lessons_student.yml')
def get_lessons_for_student(student_id):
    # TODO: request.args.get('date-from'), request.args.get('date-to')
    return model.lessons.for_student(student_id)

@lessons.route('/group/<int:group_id>')
@swag_from('swagger/lessons_group.yml')
def get_lessons_for_group(group_id):
    return model.lessons.for_group(group_id)