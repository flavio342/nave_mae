from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):

    attended = IntegerField(
        'attended'
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