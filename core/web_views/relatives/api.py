from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail, relative_token_serializer
from core.models import Relative

from core.web_views.relatives.serializer import serialize
from core.web_views.relatives.form import RegisterForm, LoginForm
from core.web_views.relatives.query import get_by_email
from core.common import relative_token_required, upload_file
from core import API_URL

class RelativeProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            photo = upload_file(request.files['photo'])

            obj = Relative(
                name=form.name.data,
                cpf=form.cpf.data,
                phone=form.phone.data,
                email=form.email.data,
                password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
                photo=photo,
                active=True
            )

            db.session.add(obj)
            db.session.commit()

            """token = relative_token_serializer.dumps(form.email.data, salt='confirm-email')
            
            msg = Message(
                '82Hack - Confirmação de Cadastro',
                sender=app.config['MAIL_USERNAME'],
                recipients=[form.email.data]
            )
            msg.html = "<a href='" + API_URL + "confirm_email/" + \
                token + "'>Clique aqui para confirmar seu cadastro!</a>"
            mail.send(msg)"""

            return {'success': True}

        else:
            print(form.errors)
            return {'success': False, "errors": form.errors}


class RelativeLogin(Resource):

    def post(self):

        form = LoginForm()

        if form.validate_on_submit():
            
            obj = get_by_email("flavioribeiro342+1586234068@gmail.com")
            if obj:

                if bcrypt.check_password_hash(obj.password, form.password.data):

                    token = jwt.encode(
                        {
                            'user': obj.email,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                        },
                        app.config['RELATIVE_TOKEN_SECRET_KEY']
                    ).decode('UTF-8')

                    return {'success': True, 'token': token}

                else:
                    return {'success': False, "errors": {"password": ["Senha incorreta."]}}

            else:

                return {'success': False, "errors": {"email": ["Email não cadastrado."]}}

        else:

            return {'success': False, "errors": form.errors}