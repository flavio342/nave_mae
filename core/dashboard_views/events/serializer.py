
from core.dashboard_views.events.query import get_class_by_id, get_student_by_id
from core import API_URL
def serialize(obj):

    obj_class = get_class_by_id(obj.class_id)

    return {
        "repr": str(obj),
        "id": obj.id,
        "photo": API_URL + "uploads/" + obj.photo,
        "name": obj.name,
        "description": obj.description,
        "class": obj_class.name,
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        print(obj)
        res.append(serialize(obj))
    return res
