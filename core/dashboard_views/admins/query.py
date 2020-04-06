from core.models import Admin


def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()
