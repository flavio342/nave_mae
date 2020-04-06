from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):

    name = StringField(
        'name',
        validators=[
            DataRequired(message="Obrigatório."),
            Length(min=5, max=250,
                   message="Deve ter entre 5 e 250 caracteres.")
        ]
    )

    photo = StringField(
        'photo',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    institution_id = IntegerField(
        'institution_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )