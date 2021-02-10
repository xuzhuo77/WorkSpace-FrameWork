# tasks.py
from celery import Celery
import time
app = Celery(
    'tasks',  # 当前模块的名字
    broker='amqp://xuzhuo:xuzhuo77!@129.211.61.116:5672//',  # 消息队列的url,
    # broker='redis://:xuzhuo77!@129.211.61.116:60379/0',  # 消息队列的url,
    backend='redis://:xuzhuo77!@129.211.61.116:60379/0'
)
# 创建任务
@app.task
def task_add(a, b):
    n = a + b
    print(n)
    return n

def get_result(task_id):
    result = app.AsyncResult(task_id)
    return result.result

if __name__ == '__main__':
    # add(10, 5)
    # 调用任务
    task_add.delay(10, 5)
    print('程序执行结束')