
from core.models import Institution


def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()