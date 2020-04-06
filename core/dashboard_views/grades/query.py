
from core.models import Grade, Class, Student


def get_all():
    return Grade.query.all()


def get_by_id(id):
    return Grade.query.filter_by(id=id).first()


def get_class_by_id(id):
    return Class.query.filter_by(id=id).first()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()