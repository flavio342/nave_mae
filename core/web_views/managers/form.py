from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from core.models import Manager

class RegisterForm(FlaskForm):

    name = StringField(
        'name',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=5, max=250,
                   message="Deve ter entre 5 e 250 caracteres.")
        ]
    )

    cpf = StringField(
        'cpf',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=11, max=11, message="Deve ter 11 caracteres.")
        ]
    )

    phone = StringField(
        'phone',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=10, max=11, message="Deve ter entre 10 e 11 caracteres.")
        ]
    )

    email = StringField(
        'email',
        validators=[
            DataRequired(message="Obrigatório."),
            Email(message="Email inválido.")
        ]
    )

    photo = StringField(
        'photo',
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

    confirm_password = PasswordField(
        'confirm_password',
        validators=[
            DataRequired(message="Obrigatório."),
            EqualTo('password', message="Confirmação diferente de senha.")
        ]
    )

    institution_name = StringField(
        'institution_name',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=5, max=250,
                   message="Deve ter entre 5 e 250 caracteres.")
        ]
    )

    def validate_email(self, email):

        obj = Manager.query.filter_by(email=email.data).first()
        if obj:
            raise ValidationError(
                'Já existe uma conta cadastrada com este email.')


class LoginForm(FlaskForm):

    email = StringField(
        'email',
        validators=[
            DataRequired(message="Obrigatório."),
            Email(message="Email inválido.")
        ]
    )

    password = PasswordField(
        'password',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=6, message="Deve ter no mínimo 6 caracteres.")
        ]
    )