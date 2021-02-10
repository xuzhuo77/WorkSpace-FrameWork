from flask import Blueprint


blueprint_tushare = Blueprint('tushare', __name__)

from zhak_restful_projets.TushareService import TushareUrls

