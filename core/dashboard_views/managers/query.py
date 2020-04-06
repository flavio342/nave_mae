
from core.models import Manager, Institution


def get_all():
    return Manager.query.all()


def get_by_id(id):
    return Manager.query.filter_by(id=id).first()


def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()