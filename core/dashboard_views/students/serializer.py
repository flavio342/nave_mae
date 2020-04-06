from core import API_URL

def serialize(obj):

    institutions = ""
    for count, i in enumerate(obj.institutions):
        institutions += i.name
        if count < len(obj.institutions)-1:
            institutions += " - "

    classes = ""
    for count, c in enumerate(obj.classes):
        classes += c.name
        if count < len(obj.classes)-1:
            classes += " - "

    relatives = ""
    for count, r in enumerate(obj.relatives):
        relatives += r.name
        if count < len(obj.relatives)-1:
            relatives += " - "

    return {
        "repr": str(obj),
        "id": obj.id,
        "name": obj.name,
        "cpf": obj.cpf,
        "phone": obj.phone,
        "email": obj.email,
        "photo": API_URL + "uploads/" + obj.photo,
        "institutions": institutions,
        "classes": classes,
        "relatives": relatives
    }

def serialize_list(objs):
    res = []
    for obj in objs:
        res.append(serialize(obj))
    return res
