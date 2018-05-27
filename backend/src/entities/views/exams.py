
from flask import Blueprint, jsonify, request

from ..models.exam import Exam, ExamSchema

exams_page = Blueprint('exams_page', __name__,
                        template_folder='templates')

@exams_page.route('/exams')
def get_exams():
    # fetching from the database
    exams = {}
    with Exam() as examModel:
        exam_objects = examModel.getQuery().all()
        # transforming into JSON-serializable objects
        schema = ExamSchema(many=True)
        exams = schema.dump(exam_objects)
    # serializing as JSON
    return jsonify(exams.data)


# @exams_page.route('/exams', methods=['POST'])
# def add_exam():
#     # mount exam object
#     posted_exam = ExamSchema(only=('title', 'description'))\
#         .load(request.get_json())

#     exam = Exam(**posted_exam.data, created_by="HTTP post request")

#     # persist exam
#     session = Session()
#     session.add(exam)
#     session.commit()

#     # return created exam
#     new_exam = ExamSchema().dump(exam).data
#     session.close()
#     return jsonify(new_exam), 201