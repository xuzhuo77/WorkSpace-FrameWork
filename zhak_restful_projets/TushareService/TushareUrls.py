#coding:utf-8
from flask_restful import  Api
from zhak_restful_projets.TushareService import blueprint_tushare
from zhak_restful_projets.TushareService.TushareController import TushareS





api_url = Api(blueprint_tushare)
api_url.add_resource(TushareS, '/tushareList/<string:id>')
