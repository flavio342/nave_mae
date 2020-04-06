
from core.models import Event, Class, Student


def get_all():
    return Event.query.all()


def get_by_id(id):
    return Event.query.filter_by(id=id).first()


def get_class_by_id(id):
    return Class.query.filter_by(id=id).first()

def get_student_by_id(id):
    return Student.query.filter_by(id=id).first()