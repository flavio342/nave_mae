from core import API_URL

def serialize(obj):
    return {
        "repr": str(obj),
        "id": obj.id,
        "name": obj.name,
        "cpf": obj.cpf,
        "phone": obj.phone,
        "email": obj.email,
        "photo": API_URL + "uploads/" + obj.photo,
        "active": obj.active
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        res.append(serialize(obj))
    return res
