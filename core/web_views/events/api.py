from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Event

from core.web_views.events.serializer import serialize
from core.web_views.events.form import RegisterForm
from core.web_views.events.query import get_class_by_id, get_student_by_id
from core.common import relative_token_required, upload_file


class EventProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            photo = upload_file(request.files['photo'])

            obj = Event(
                name=form.name.data,
                date=form.date.data,
                description=form.description.data,
                photo=photo
            )
            
            class_obj = get_class_by_id(form.class_id.data)
            if class_obj:

                print(class_obj.events)

                class_obj.events.append(obj)

                db.session.add_all([class_obj, obj])
                db.session.commit()
                
                return {'success': True}

            else:
                return {'success': False, "errors": {"class_id": ["Turma não existe"]}}

        else:

            return {'success': False, "errors": form.errors}