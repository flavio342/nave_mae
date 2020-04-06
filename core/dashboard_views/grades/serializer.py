
from core.dashboard_views.grades.query import get_class_by_id, get_student_by_id

def serialize(obj):

    obj_class = get_class_by_id(obj.class_id)

    student = get_student_by_id(obj.student_id)

    return {
        "repr": str(obj),
        "id": obj.id,
        "name": obj.name,
        "points": obj.points,
        "feedback": obj.feedback,
        "class": obj_class.name,
        "student": student.name,
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        print(obj)
        res.append(serialize(obj))
    return res
