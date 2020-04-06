
from core.models import Institution, Institution


def get_all():
    return Institution.query.all()


def get_by_id(id):
    return Institution.query.filter_by(id=id).first()