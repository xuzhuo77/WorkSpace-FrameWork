from flask import Blueprint

from RegisterService.RegisterService import RegisterService

registerController = Blueprint("Register", __name__)
register_service = RegisterService()


