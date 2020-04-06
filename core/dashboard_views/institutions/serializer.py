
from core.dashboard_views.managers.query import get_institution_by_id
from core import API_URL

def serialize(obj):

    return {
        "repr": str(obj),
        "id": obj.id,
        "name": obj.name,
        "photo": API_URL + "uploads/" + obj.photo
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        res.append(serialize(obj))
    return res
