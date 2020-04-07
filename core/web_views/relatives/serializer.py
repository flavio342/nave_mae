from core import API_URL

def serialize(obj):
    
    students = []
    for s in obj.students:

        student = {
            "id": s.id,
            "name": s.name,
            "photo": API_URL + "uploads/" + s.photo,
            "institutions": []   
        }

        for i in s.institutions:
            institution = {
                'id': i.id,
                'name': i.name,
                'photo': API_URL + "uploads/" + i.photo,
                'classes': []
            }

            for c in s.classes:
                if c.institution_id == i.id:

                    class_obj = {
                        'id': c.id,
                        'name': c.name,
                        'photo': API_URL + "uploads/" + c.photo,
                        'grades': [],
                        'attendances': [],
                        'events': []
                    }
                    
                    events = []
                    for e in c.events:
                        events.append({
                            "id": e.id,
                            "name": e.name,
                            "date": e.date,
                            "description": e.description,
                            "photo": API_URL + "uploads/" + e.photo
                        })

                    class_obj['events'] = events
                   
                    for g in s.grades:
                        if g.class_id == c.id:

                            grade = {
                                'id': g.id,
                                'name': g.name,
                                'points': g.points,
                                'feedback': g.feedback
                            }

                            class_obj['grades'].append(grade)

                    for a in s.attendances:
                        if a.class_id == c.id:

                            attendance = {
                                'id': a.id,
                                'attended': a.attended
                            }

                            class_obj['attendances'].append(attendance)

                    institution['classes'].append(class_obj)

            student['institutions'].append(institution)

        students.append(student)

    return {
        "user": {
            "id": obj.id,
            "name": obj.name,
            "photo": API_URL + "uploads/" + obj.photo,
        },
        "students": students
    }
