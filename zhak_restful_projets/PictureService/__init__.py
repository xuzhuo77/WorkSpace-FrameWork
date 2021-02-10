from flask import Blueprint

blueprint_picture = Blueprint('picture', __name__)
from zhak_restful_projets.PictureService import PictureUrls
