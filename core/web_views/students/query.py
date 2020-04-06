
from core.models import Institution, Student, Class, Relative


def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()

def get_class_by_id(id):
    return Class.query.filter_by(id=id).first()

def get_relative_by_id(id):
    return Relative.query.filter_by(id=id).first()