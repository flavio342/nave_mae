from core import db, app

relation_student_relative = db.Table(
    'Relation Student Relative',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('relative_id', db.Integer, db.ForeignKey('relative.id'), primary_key=True)
)

relation_student_class = db.Table(
    'Relation Student Class',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True)
)

relation_student_institution = db.Table(
    'Relation Student Institution',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('institution_id', db.Integer, db.ForeignKey('institution.id'), primary_key=True)
)

class Student(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    cpf = db.Column(
        db.String(50),
        nullable=False
    )

    phone = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(250),
        unique=True,
        nullable=False
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    grades = db.relationship('Grade', backref='student', lazy=True, cascade="all, delete-orphan")

    attendances = db.relationship('Attendance', backref='student', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.email


class Manager(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    cpf = db.Column(
        db.String(50),
        nullable=False
    )

    phone = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(250),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(250),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    institution_id = db.Column(
        db.Integer,
        db.ForeignKey('institution.id'),
        nullable=False
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    def __repr__(self):
        return self.email


class Relative(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    cpf = db.Column(
        db.String(50),
        nullable=False
    )

    phone = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(250),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(250),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    students = db.relationship(Student, secondary=relation_student_relative, backref='relatives')

    def __repr__(self):
        return self.email


class Admin(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(250),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(250),
        nullable=False
    )


class Institution(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    managers = db.relationship('Manager', backref='institution', lazy=True, cascade="all, delete-orphan")

    classes = db.relationship('Class', backref='institution', lazy=True, cascade="all, delete-orphan")

    students = db.relationship(Student, secondary=relation_student_institution, backref='institutions')

    def __repr__(self):
        return self.name


class Class(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    institution_id = db.Column(
        db.Integer,
        db.ForeignKey('institution.id'),
        nullable=False
    )

    students = db.relationship(Student, secondary=relation_student_class, backref='classes')

    grades = db.relationship('Grade', backref='class', lazy=True, cascade="all, delete-orphan")

    attendances = db.relationship('Attendance', backref='class', lazy=True, cascade="all, delete-orphan")

    events = db.relationship('Event', backref='class', lazy=True, cascade="all, delete-orphan")


class Grade(db.Model):


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    points = db.Column(
        db.Float,
        nullable=False
    )

    feedback = db.Column(
        db.String(500),
        nullable=True
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey('class.id'),
        nullable=False
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id'),
        nullable=False
    )

    def __repr__(self):
        return self.name


class Attendance(db.Model):


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    attended = db.Column(
        db.Integer,
        nullable=False
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey('class.id'),
        nullable=False
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id'),
        nullable=False
    )

    def __repr__(self):
        return str(self.id)


class Event(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(250),
        nullable=False
    )

    description = db.Column(
        db.String(500),
        nullable=True
    )

    photo = db.Column(
        db.String(250),
        nullable=True
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey('class.id'),
        nullable=False
    )

    date = db.Column(
        db.String(250),
        nullable=True
    )

