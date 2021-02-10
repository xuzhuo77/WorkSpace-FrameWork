
from zhak_restful_projets.myapp import api

from flask_restful import Resource


class TushareS(Resource):
    def get(self,id):
        return 'this is data list'+str(id)