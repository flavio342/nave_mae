from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, IntegerField, FloatField
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

    points = FloatField(
        'points',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    feedback = StringField(
        'feedback',
        validators=[
            Length(max=500,
                   message="Deve no máximo 500 caracteres.")
        ]
    )

    class_id = IntegerField(
        'class_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    student_id = IntegerField(
        'student_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )