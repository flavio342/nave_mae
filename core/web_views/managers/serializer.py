from core import API_URL

from core.web_views.managers.query import get_institution_by_id

def serialize(obj):

    institution = get_institution_by_id(obj.institution_id)

    relatives = []
    for s in institution.students:
        for r in s.relatives:

            found_r = False
            for rel in relatives:
                if rel["id"] == r.id:
                    found_r = rel

            if found_r:
                found_r["students"].append({
                    "id": s.id,
                    "name": s.name,
                    "photo":  API_URL + "uploads/" + s.photo
                })

            else:
                relatives.append({
                    "id": r.id,
                    "name": r.name,
                    "photo": API_URL + "uploads/" + r.photo,
                    "students": [
                        {
                            "id": s.id,
                            "name": s.name,
                            "photo":  API_URL + "uploads/" + s.photo
                        }
                    ]
                })


    return {
        "id": obj.id,
        "name": obj.name,
        "cpf": obj.cpf,
        "phone": obj.phone,
        "email": obj.email,
        "photo": API_URL + "uploads/" + obj.photo,
        "active": obj.active,
        "institution": {
            "id": institution.id,
            "name": institution.name,
            "photo": API_URL + "uploads/" + institution.photo
        },
        "relatives": relatives
    }
