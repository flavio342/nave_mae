from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from core.models import Student

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

    def validate_email(self, email):

        obj = Student.query.filter_by(email=email.data).first()
        if obj:
            raise ValidationError(
                'Já existe uma conta cadastrada com este email.')


class StudentInstitutionForm(FlaskForm):

    student_id = IntegerField(
        'student_id',
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

class StudentClassForm(FlaskForm):

    student_id = IntegerField(
        'student_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    class_id = IntegerField(
        'class_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

class StudentRelativeForm(FlaskForm):

    student_id = IntegerField(
        'student_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )

    relative_id = IntegerField(
        'relative_id',
        validators=[
            DataRequired(message="Obrigatório.")
        ]
    )