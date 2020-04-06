from flask import send_file
from flask_restful import Resource
import os

from core import app


class Uploads(Resource):

    def get(self, filename):

        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype='image/gif')
