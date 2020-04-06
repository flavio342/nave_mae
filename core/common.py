from flask import request, abort
from functools import wraps
import jwt
from werkzeug.utils import secure_filename
import os
import time

from core import app
from core.models import Manager, Admin, Relative


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        try:
            
            token = request.headers['Authorization']

            decoded_token = jwt.decode(token, app.config['ADMIN_TOKEN_SECRET_KEY'])
            decoded_user = decoded_token['user']

            user = Admin.query.filter_by(username=decoded_user).first()

            if user:
                kwargs['user'] = user
            else:
                return abort(401)

        except:
            return abort(401)

        print(kwargs)
        return f(*args, **kwargs)

    return decorated

def manager_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        try:
            
            token = request.headers['Authorization']

            decoded_token = jwt.decode(token, app.config['MANAGER_TOKEN_SECRET_KEY'])
            decoded_user = decoded_token['user']

            user = Manager.query.filter_by(email=decoded_user).first()

            if user:
                kwargs['user'] = user
            else:
                return abort(401)

        except:
            return abort(401)

        print(kwargs)
        return f(*args, **kwargs)

    return decorated

def relative_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        try:
            
            token = request.headers['Authorization']

            decoded_token = jwt.decode(token, app.config['RELATIVE_TOKEN_SECRET_KEY'])
            decoded_user = decoded_token['user']

            user = Relative.query.filter_by(email=decoded_user).first()

            if user:
                kwargs['user'] = user
            else:
                return abort(401)

        except:
            return abort(401)

        print(kwargs)
        return f(*args, **kwargs)

    return decorated


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(f):

    if f and allowed_file(f.filename):

        filename = secure_filename(
            str(time.time()) + "." + f.filename.split(".")[-1])
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return filename

    else:
        return None


def delete_file(filename):
    try:
        os.remove(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
    except:
        return
