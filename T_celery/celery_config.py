#-*-coding=utf-8-*-
from __future__ import absolute_import
from kombu import Queue
from celery.schedules import crontab
class CeleryConfig:
    # 中间件
    BROKER_URL = 'redis://:xuzhuo77!@129.211.61.116:60379/1'
    # BROKER_URL = 'amqp://xuzhuo:xuzhuo77!@129.211.61.116:5672//'
    # 结果存储
    CELERY_RESULT_BACKEND = 'redis://:xuzhuo77!@129.211.61.116:60379/0'
    # 默认worker队列
    CELERY_DEFAULT_QUEUE = 'default'
    # 异步任务
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True
    CELERY_IMPORTS = (

        "T_celery.celery_tasks"
    )
    from datetime import timedelta
    CELERY_QUEUES = (  # 定义任务队列
        Queue('default', routing_key='task.#'),  # 路由键以"task."开头的消息都进default队列
        Queue('web_tasks', routing_key='web.#'),  # 路由键以"web."开头的消息都进web_tasks队列
    )
    # celery beat
    CELERYBEAT_SCHEDULE = {
        'celery_app.task.task1': {
            'task': 'T_celery.celery_tasks.c_add',
            'schedule': timedelta(seconds=20),
            'args': (1, 10)
        },
        'celery_app.task.task2': {
            'task': 'T_celery.celery_tasks.c_sub',
            'schedule': crontab(minute='*/2'),
            'args': (99,12)
        }
    }