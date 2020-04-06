from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Grade

from core.web_views.grades.serializer import serialize
from core.web_views.grades.form import RegisterForm
from core.web_views.grades.query import get_class_by_id, get_student_by_id
from core.common import relative_token_required, upload_file


class GradeProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            obj = Grade(
                name=form.name.data,
                points=form.points.data,
                feedback=form.feedback.data
            )
            
            class_obj = get_class_by_id(form.class_id.data)
            if class_obj:

                student_obj = get_student_by_id(form.student_id.data)
                if student_obj:

                    print(class_obj.grades)

                    student_obj.grades.append(obj)
                    class_obj.grades.append(obj)

                    db.session.add_all([class_obj, student_obj, obj])
                    db.session.commit()
                    
                    return {'success': True}

                else:
                    return {'success': False, "errors": {"student_id": ["Aluno não existe"]}}


            else:
                return {'success': False, "errors": {"class_id": ["Turma não existe"]}}

        else:

            return {'success': False, "errors": form.errors}