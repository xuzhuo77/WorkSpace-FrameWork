#coding:utf-8
from flask import Flask

from zhak_restful_projets.AccessoryFileService import blueprint_accessory_file
from zhak_restful_projets.PictureService import blueprint_picture
from zhak_restful_projets.TushareService import blueprint_tushare

app_xujingtong = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            )



app_xujingtong.register_blueprint(blueprint_tushare)
app_xujingtong.register_blueprint(blueprint_picture)
app_xujingtong.register_blueprint(blueprint_accessory_file)

if __name__ == '__main__':
    app_xujingtong.run(host='0.0.0.0', port=5000, debug=True)