from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Class

from core.web_views.classes.serializer import serialize
from core.web_views.classes.form import RegisterForm
from core.web_views.classes.query import get_institution_by_id
from core.common import relative_token_required, upload_file


class ClassProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            photo = upload_file(request.files['photo'])

            obj = Class(
                name=form.name.data,
                photo=photo
            )

            institution_obj = get_institution_by_id(form.institution_id.data)
            if institution_obj:
                
                institution_obj.classes.append(obj)

                db.session.add(obj)
                db.session.add(institution_obj)
                db.session.commit()

                return {'success': True}

            else:

                return {'success': False, "errors": {"institution_id": ["Instituição não existe"]}}

        else:

            return {'success': False, "errors": form.errors}