# -*- coding: utf-8 -*-
# https://programtalk.com/python-examples/flask.views.MethodView/

# from Application import app
from flask import Flask
from WSGICopyBody import WSGICopyBody
from xujingtong_projets.TushareService.TushareController import TushareBluePrint, scheduler, SchedulerConfigTushare


app = Flask(__name__)
app.wsgi_app = WSGICopyBody(app.wsgi_app)

app.register_blueprint(TushareBluePrint, url_prefix='/tushare')

app.config.from_object(SchedulerConfigTushare)

if __name__ == '__main__':
    scheduler.init_app(app=app)
    scheduler.start()
    app.run(host="0.0.0.0", port=50, debug=True)
