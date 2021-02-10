from werkzeug.utils import secure_filename
from flask import request, jsonify, send_from_directory, abort

import base64
import os
import time

UPLOAD_FOLDER = 'upload'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = 'D:\\WorkSpace-FrameWork\\Storage'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])


class FlaskAccessFileUtil():

    # 用于判断文件后缀
    def _allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def api_upload(self, request_file, fileParam):
        # file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        file_dir = os.path.join(basedir, fileParam.module_name)

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
        if request_file and self._allowed_file(request_file.filename):  # 判断是否是允许上传的文件类型
            fname = secure_filename(request_file.filename)
            # print(fname)

            ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
            unix_time = int(time.time())
            new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
            request_file.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
            token = base64.b64encode(new_filename.encode())
            if isinstance(token, bytes):
                token = str(token, encoding='utf-8')

            return {"errno": 0, "errmsg": "上传成功", "token": token}
        else:
            return {"errno": 1001, "errmsg": "上传失败"}

    def download(self, accessfile):
            file_name= base64.b64decode(accessfile.token).decode()
            file_storge = os.path.join(basedir, accessfile.module_name)

            file_dir=os.path.join(file_storge,file_name)
            if os.path.isfile(file_dir):

                return send_from_directory(file_storge, file_name, as_attachment=True)
            abort(404)


class FileParam:
    def __init__(self, guid, module_name, filename):
        self.guid = guid
        self.module_name = module_name
        self.filename = filename
