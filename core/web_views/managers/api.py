from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired
import json

from core import db, bcrypt, app, mail, manager_token_serializer
from core.models import Manager, Institution

from core.web_views.managers.serializer import serialize
from core.web_views.managers.form import RegisterForm, LoginForm
from core.web_views.managers.query import get_institution_by_name, get_by_email
from core.common import manager_token_required, upload_file
from core import API_URL

class ManagerProfile(Resource):

    @manager_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            photo = upload_file(request.files['photo'])

            manager_obj = Manager(
                name=form.name.data,
                cpf=form.cpf.data,
                phone=form.phone.data,
                email=form.email.data,
                password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
                photo=photo,
                active=True
            )

            institution_obj = get_institution_by_name(form.institution_name.data)
            if not institution_obj:
                
                institution_photo = upload_file(request.files['institution_photo'])
                institution_obj = Institution(
                    name=form.institution_name.data,
                    photo=institution_photo
                )

            institution_obj.managers.append(manager_obj)

            db.session.add(institution_obj)
            db.session.add(manager_obj)
            db.session.commit()

            """token = manager_token_serializer.dumps(form.email.data, salt='confirm-email')
            
            msg = Message(
                '82Hack - Confirmação de Cadastro',
                sender=app.config['MAIL_USERNAME'],
                recipients=[form.email.data]
            )
            msg.html = "<a href='" + API_URL + "/confirm_email/" + \
                token + "'>Clique aqui para confirmar seu cadastro!</a>"
            mail.send(msg)"""

            return {'success': True}

        else:
            print(form.errors)
            return {'success': False, "errors": form.errors}


class ManagerLogin(Resource):

    def post(self):

        form = LoginForm()

        if form.validate_on_submit():
            
            obj = get_by_email("flavioribeiro342+1585985497@gmail.com")
            if obj:

                if bcrypt.check_password_hash(obj.password, form.password.data):

                    token = jwt.encode(
                        {
                            'user': obj.email,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                        },
                        app.config['MANAGER_TOKEN_SECRET_KEY']
                    ).decode('UTF-8')

                    return {'success': True, 'token': token}

                else:
                    return {'success': False, "errors": {"password": ["Senha incorreta."]}}

            else:

                return {'success': False, "errors": {"email": ["Email não cadastrado."]}}

        else:

            return {'success': False, "errors": form.errors}