
from core.models import Class, Student


def get_class_by_id(id):
    return Class.query.filter_by(id=id).first()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()