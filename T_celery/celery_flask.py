from flask import Flask,jsonify,request,make_response
from T_celery.tasks import task_add, get_result
from T_celery.celery_tasks import get_result,c_add,c_sub

import json
app = Flask(__name__)

@app.route('/')
def index():
    a=task_add.delay(1,2)
    return str(a.task_id)+"激活邮件已发送， 请注意查收"

@app.route('/add')
def add():
    a=c_add.delay(100,22)
    return str(a.task_id)+"add 测试"
@app.route('/sub')
def sub():
    a=c_sub.delay(300,20)
    return str(a.task_id)+"sub 测试"

@app.route('/task_result/<string:task_id>',methods = ["GET","POST"])
def task_result(task_id):
    # data = json.loads(request.get_data())
    # task_id = data['task_id']
    result = get_result(task_id)

    return make_response(jsonify(result=result,task_id=task_id))



if __name__ == '__main__':
    app.run()