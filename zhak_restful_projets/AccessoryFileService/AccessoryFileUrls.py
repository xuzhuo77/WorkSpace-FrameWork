#coding:utf-8
from flask_restful import  Api

from zhak_restful_projets.AccessoryFileService.AccessoryController import AccessoryFileList, Upload
from zhak_restful_projets.TushareService import blueprint_tushare

api_url = Api(blueprint_tushare)
api_url.add_resource(AccessoryFileList, '/accessoryFiles')
api_url.add_resource(Upload, '/upload')
