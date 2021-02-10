from flask import Blueprint

from AccessFileService.AccessFileService import AccessFileService
from Utils import UniqueIdUtil
from Utils.AccessFileUtil import FileParam
from Utils.ReturnUtil import ReturnUtil
from flask import request

accessFileController = Blueprint("accessFile", __name__)


@accessFileController.route('/upload', methods=["POST"], strict_slashes=False)
def upload():
    if request.method == 'POST':
        requestfile = request.files['myfile']
        fp = FileParam(UniqueIdUtil.gen_guid(), request.form.get("moduleName"), requestfile.filename)
        result = AccessFileService().save_file(requestfile, fp)
        return ReturnUtil().ok(result)


@accessFileController.route('/find_by_id', methods=['GET'])
def find_by_id():
    id = request.args.get("id")  # 获取  get  参数
    entity = AccessFileService().find_by_id(id)
    return ReturnUtil().ok(entity);


@accessFileController.route('/find_by_guid', methods=['GET'])
def find_by_guid():
    guid = request.form.get("guid")  # 获取  get  参数
    entity = AccessFileService().find_by_guid(guid)
    return ReturnUtil().ok(entity);


@accessFileController.route('/download', methods=['GET'])
def download():
    if request.method == "GET":
        guid=request.args.get("guid")
        # guid = request.form.get("guid")  # 获取  get  参数
        file = AccessFileService().download(guid)
        return file
