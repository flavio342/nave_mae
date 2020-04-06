from core.models import Relative


def get_by_email(email):
    return Relative.query.filter_by(email=email).first()
