from zhak_restful_projets.myapp import api

from flask_restful import Resource

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class AccessoryFileList(Resource):
    def get(self):
        return 'this is data list'


class Upload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']
        return file.name, 201
