
from core.models import Institution, Manager

def get_by_email(email):
    return Manager.query.filter_by(email=email).first()

def get_institution_by_name(name):
    return Institution.query.filter_by(name=name).first()

def get_institution_by_id(id):
    return Institution.query.filter_by(id=id).first()