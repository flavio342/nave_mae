from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = False


package_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(package_dir, 'site.db')
app.config['SQLALCHEMY_DATABASE_URI'] = ''.join(['sqlite:///', db_dir])
app.config['ADMIN_TOKEN_SECRET_KEY'] = '7ba7a30f-04f8-4be1-8f64-ad024d655b69'
app.config['RELATIVE_TOKEN_SECRET_KEY'] = 'f7cacfb6-6c23-4876-b9a3-585d88c43709'
app.config['MANAGER_TOKEN_SECRET_KEY'] = '7c9bdf55-867e-482e-9940-5f8958d76e89'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '82hack2020@gmail.com'
app.config['MAIL_PASSWORD'] = '82covid19'
app.config['UPLOAD_FOLDER'] = '/home/flavio342/Desktop/82hack/backend/core/uploads'

mail = Mail(app)

manager_token_serializer = URLSafeTimedSerializer(app.config['MANAGER_TOKEN_SECRET_KEY'])
relative_token_serializer = URLSafeTimedSerializer(app.config['RELATIVE_TOKEN_SECRET_KEY'])

CORS(app)

db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

API_URL = "http://flavio342-af518b0d.localhost.run/"

# DASHBOARD

from core.dashboard_views.admins.api import Admins, AdminLogin
from core.dashboard_views.managers.api import Managers, DeleteManagers
from core.dashboard_views.students.api import Students, DeleteStudents
from core.dashboard_views.relatives.api import Relatives, DeleteRelatives
from core.dashboard_views.institutions.api import Institutions, DeleteInstitutions
from core.dashboard_views.classes.api import Classes, DeleteClasses
from core.dashboard_views.grades.api import Grades, DeleteGrades
from core.dashboard_views.attendances.api import Attendances, DeleteAttendances
from core.dashboard_views.events.api import Events, DeleteEvents


api.add_resource(Admins, '/admin')
api.add_resource(AdminLogin, '/login_admin')

api.add_resource(Managers, '/managers')
api.add_resource(DeleteManagers, '/delete_managers')

api.add_resource(Students, '/students')
api.add_resource(DeleteStudents, '/delete_students')

api.add_resource(Relatives, '/relatives')
api.add_resource(DeleteRelatives, '/delete_relatives')

api.add_resource(Institutions, '/institutions')
api.add_resource(DeleteInstitutions, '/delete_institutions')

api.add_resource(Classes, '/classes')
api.add_resource(DeleteClasses, '/delete_classes')

api.add_resource(Grades, '/grades')
api.add_resource(DeleteGrades, '/delete_grades')

api.add_resource(Attendances, '/attendances')
api.add_resource(DeleteAttendances, '/delete_attendances')

api.add_resource(Events, '/events')
api.add_resource(DeleteEvents, '/delete_events')


# SITE

from core.web_views.managers.api import ManagerProfile, ManagerLogin
from core.web_views.students.api import StudentProfile, StudentInstitution, StudentClass, StudentRelative
from core.web_views.relatives.api import RelativeProfile, RelativeLogin
from core.web_views.classes.api import ClassProfile
from core.web_views.grades.api import GradeProfile
from core.web_views.attendances.api import AttendanceProfile
from core.web_views.events.api import EventProfile

api.add_resource(ManagerProfile, '/manager')
api.add_resource(ManagerLogin, '/manager_login')

api.add_resource(StudentProfile, '/student')
api.add_resource(StudentInstitution, '/student_institution')
api.add_resource(StudentClass, '/student_class')
api.add_resource(StudentRelative, '/student_relative')

api.add_resource(RelativeProfile, '/relative')
api.add_resource(RelativeLogin, '/relative_login')

api.add_resource(ClassProfile, '/class')

api.add_resource(GradeProfile, '/grade')

api.add_resource(AttendanceProfile, '/attendance')

api.add_resource(EventProfile, '/event')

# COMMON

from core.common_views.uploads.api import Uploads

api.add_resource(Uploads, '/uploads/<filename>')


app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('chat_in')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('chat_broadcast', json)