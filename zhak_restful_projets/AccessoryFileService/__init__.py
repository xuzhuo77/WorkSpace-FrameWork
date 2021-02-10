from flask import Blueprint

blueprint_accessory_file = Blueprint('accessory_file', __name__)
from zhak_restful_projets.AccessoryFileService import AccessoryFileUrls
