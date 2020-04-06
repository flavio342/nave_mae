from flask import request
from flask_restful import Resource
import jwt
import datetime

from core import db, bcrypt, app
from core.models import Admin
from core.dashboard_views.admins.form import RegisterForm, LoginForm
from core.dashboard_views.admins.query import get_admin_by_username


class Admins(Resource):

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            admin = Admin(
                username=form.username.data,
                password=bcrypt.generate_password_hash(
                    form.password.data).decode('utf-8')
            )

            db.session.add(admin)
            db.session.commit()

            return {'success': True}

        else:

            return {'success': False, "errors": form.errors}


class AdminLogin(Resource):

    def post(self):

        form = LoginForm()

        if form.validate_on_submit():

            admin = get_admin_by_username(form.username.data)

            if admin:

                if bcrypt.check_password_hash(admin.password, form.password.data):

                    token = jwt.encode(
                        {
                            'user': admin.username,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                        },
                        app.config['ADMIN_TOKEN_SECRET_KEY']
                    ).decode('UTF-8')

                    return {'success': True, 'token': token}

                else:
                    return {'success': False, "errors": {"password": ["Senha incorreta."]}}

            else:

                return {'success': False, "errors": {"username": ["Username não cadastrado."]}}

        else:

            return {'success': False, "errors": form.errors}
