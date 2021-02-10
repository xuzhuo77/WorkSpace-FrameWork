#coding:utf-8
from flask_restful import  Api

from zhak_restful_projets.PictureService import blueprint_picture
from zhak_restful_projets.PictureService.PictureController import PictureList,PictureUpload

api_url = Api(blueprint_picture)
api_url.add_resource(PictureList, '/pictures')
api_url.add_resource(PictureUpload, '/picture/upload')
