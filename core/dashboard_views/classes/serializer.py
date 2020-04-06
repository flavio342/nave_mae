
from core.dashboard_views.classes.query import get_institution_by_id
from core import API_URL

def serialize(obj):

    institution = get_institution_by_id(obj.institution_id)

    return {
        "repr": str(obj),
        "id": obj.id,
        "name": obj.name,
        "photo": API_URL + "uploads/" + obj.photo,
        "institution_name": institution.name
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        res.append(serialize(obj))
    return res
