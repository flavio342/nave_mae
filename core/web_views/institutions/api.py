from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Institution, Institution

from core.web_views.institutions.serializer import serialize
from core.web_views.institutions.form import RegisterForm
from core.common import relative_token_required


class InstitutionProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)