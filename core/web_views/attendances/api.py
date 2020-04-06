from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Attendance

from core.web_views.attendances.serializer import serialize
from core.web_views.attendances.form import RegisterForm
from core.web_views.attendances.query import get_class_by_id, get_student_by_id
from core.common import relative_token_required, upload_file


class AttendanceProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()
        if form.validate_on_submit():

            print("-------")
            print(form.attended)
            print(form.attended.data)

            obj = Attendance(
                attended=form.attended.data
            )

            class_obj = get_class_by_id(form.class_id.data)
            if class_obj:

                student_obj = get_student_by_id(form.student_id.data)
                if student_obj:

                    print(class_obj.attendances)

                    student_obj.attendances.append(obj)
                    class_obj.attendances.append(obj)

                    db.session.add_all([class_obj, student_obj, obj])
                    db.session.commit()

                    return {'success': True}

                else:
                    return {'success': False, "errors": {"student_id": ["Aluno não existe"]}}


            else:
                return {'success': False, "errors": {"class_id": ["Turma não existe"]}}

        else:
            print(form.errors)
            return {'success': False, "errors": form.errors}