from flask import Blueprint, request
from flasgger import swag_from

lessons = Blueprint('lessons',  __name__, url_prefix='/lessons')

@lessons.route('/student/<int:student_id>')
@swag_from('swagger/lessons_student.yml')
def get_lessons_for_student(student_id):
    return "I am student with id no {0} from {1} to {2}".format(student_id, request.args.get('date-from'), request.args.get('date-to'))