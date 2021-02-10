
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage

from Utils.ReturnUtil import ReturnUtil
from zhak_restful_projets.PictureService.PictureService import PictureService

picture_service=PictureService()

class PictureList(Resource):
    def get(self):
        list=picture_service.find_list()
        return ReturnUtil.ok(list)


class PictureUpload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']
        return file.name, 201
