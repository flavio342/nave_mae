from core import API_URL

def serialize(obj):
    return {
        "id": obj.id,
        "name": obj.name,
        "cpf": obj.cpf,
        "phone": obj.phone,
        "email": obj.email,
        "photo": API_URL + "uploads/" + obj.photo
    }
