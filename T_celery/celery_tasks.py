from T_celery.celery_app import app

@app.task(queue='default')
def c_add(x, y):
    return x + y

@app.task(queue='default')
def c_sub(x, y):
    return x - y


def get_result(task_id):
    result = app.AsyncResult(task_id)
    return result.result