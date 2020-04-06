
from core.models import Student


def get_all():
    return Student.query.all()


def get_by_id(id):
    return Student.query.filter_by(id=id).first()
