from FakeDataService.FakeDataService import FakeDataService
from flask import Blueprint
from Utils.ReturnUtil import ReturnUtil
fakeDataController = Blueprint("fakedata", __name__)


@fakeDataController.route('/profile', methods=["POST"])
def profile():
    profilex=FakeDataService().profile()
    return ReturnUtil().ok(profilex)



