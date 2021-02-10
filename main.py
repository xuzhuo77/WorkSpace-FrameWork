# -*- coding: utf-8 -*-
# https://programtalk.com/python-examples/flask.views.MethodView/

# from Application import app
from flask import Flask
from AccessFileService.AccessFileController import accessFileController
from FirstService.FirstController import firstController
from FakeDataService.FakeDataController import fakeDataController
from FirstService.FirstService import FirstService
from RegisterService.RegisterController import registerController
from WSGICopyBody import WSGICopyBody

app = Flask(__name__)
app.wsgi_app = WSGICopyBody(app.wsgi_app)

app.register_blueprint(firstController, url_prefix='/first')
app.register_blueprint(fakeDataController, url_prefix='/fakedata')
app.register_blueprint(accessFileController, url_prefix='/accessFile')
app.register_blueprint(registerController, url_prefix='/Register')

if __name__ == '__main__':
    # app = create_app()
    app.run(host="0.0.0.0", port=50, debug=True)
