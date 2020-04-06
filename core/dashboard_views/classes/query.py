
from core.models import Class, Institution


def get_all():
    return Class.query.all()


def get_by_id(id):
    return Class.query.filter_by(id=id).first()


def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()