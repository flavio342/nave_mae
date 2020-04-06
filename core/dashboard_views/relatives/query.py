
from core.models import Relative


def get_all():
    return Relative.query.all()


def get_by_id(id):
    return Relative.query.filter_by(id=id).first()
