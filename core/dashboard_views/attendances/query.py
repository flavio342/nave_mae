
from core.models import Attendance, Class, Student


def get_all():
    return Attendance.query.all()


def get_by_id(id):
    return Attendance.query.filter_by(id=id).first()


def get_class_by_id(id):
    return Class.query.filter_by(id=id).first()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()