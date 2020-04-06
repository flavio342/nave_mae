from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from core.models import Admin


class RegisterForm(FlaskForm):

    username = StringField(
        'username',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    password = PasswordField(
        'password',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=6, message="Deve ter no mínimo 6 caracteres.")
        ]
    )

    def validate_username(self, username):

        admin = Admin.query.filter_by(username=username.data).first()
        if admin:
            raise ValidationError(
                'Já existe uma conta cadastrada com este username.')


class LoginForm(FlaskForm):

    username = StringField(
        'email',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    password = PasswordField(
        'password',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=6, message="Deve ter no mínimo 6 caracteres.")
        ]
    )
