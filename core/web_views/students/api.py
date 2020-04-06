from flask import request, redirect
from flask_restful import Resource
import jwt
import datetime
from flask_mail import Message
from itsdangerous import SignatureExpired

from core import db, bcrypt, app, mail
from core.models import Student

from core.web_views.students.serializer import serialize
from core.web_views.students.form import RegisterForm, StudentInstitutionForm, StudentClassForm, StudentRelativeForm
from core.web_views.students.query import get_institution_by_id, get_student_by_id, get_class_by_id, get_relative_by_id
from core.common import relative_token_required, upload_file


class StudentProfile(Resource):

    @relative_token_required
    def get(self, user):
        return serialize(user)

    def post(self):

        form = RegisterForm()

        if form.validate_on_submit():

            photo = upload_file(request.files['photo'])

            obj = Student(
                name=form.name.data,
                cpf=form.cpf.data,
                phone=form.phone.data,
                email=form.email.data,
                photo=photo
            )

            db.session.add(obj)
            db.session.commit()

            return {'success': True, 'id': obj.id}

        else:

            return {'success': False, "errors": form.errors}


class StudentInstitution(Resource):
    
    @relative_token_required
    def post(self, user):

        form = StudentInstitutionForm()

        if form.validate_on_submit():

            institution_obj = get_institution_by_id(form.institution_id.data)
            if institution_obj:

                student_obj = get_student_by_id(form.student_id.data)
                if student_obj:
                    
                    institution_obj.students.append(student_obj)
                    db.session.add(institution_obj)
                    db.session.commit()

                    return {'success': True}
                
                else:
                    
                    return {'success': False, "errors": {"student_id": ["Aluno não existe"]}}

            else:

                return {'success': False, "errors": {"institution_id": ["Instituição não existe"]}}

        else:

            return {'success': False, "errors": form.errors}


class StudentClass(Resource):
    
    @relative_token_required
    def post(self, user):

        form = StudentClassForm()

        if form.validate_on_submit():

            class_obj = get_class_by_id(form.class_id.data)
            if class_obj:

                student_obj = get_student_by_id(form.student_id.data)
                if student_obj:
                    
                    class_obj.students.append(student_obj)
                    db.session.add(class_obj)
                    db.session.commit()

                    return {'success': True}
                
                else:
                    
                    return {'success': False, "errors": {"student_id": ["Aluno não existe"]}}

            else:

                return {'success': False, "errors": {"class_id": ["Turma não existe"]}}

        else:

            return {'success': False, "errors": form.errors}


class StudentRelative(Resource):
    
    @relative_token_required
    def post(self, user):

        form = StudentRelativeForm()

        if form.validate_on_submit():

            relative_obj = get_relative_by_id(form.relative_id.data)
            if relative_obj:

                student_obj = get_student_by_id(form.student_id.data)
                if student_obj:
                    
                    relative_obj.students.append(student_obj)
                    db.session.add(relative_obj)
                    db.session.commit()

                    return {'success': True}
                
                else:
                    
                    return {'success': False, "errors": {"student_id": ["Aluno não existe"]}}

            else:

                return {'success': False, "errors": {"relative_id": ["Familiar não existe"]}}

        else:
            print(form.errors)

            return {'success': False, "errors": form.errors}