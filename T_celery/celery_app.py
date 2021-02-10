from __future__ import absolute_import
from celery import Celery
from T_celery import celery_config
from T_celery.celery_config import CeleryConfig

app = Celery('celery_app')
app.config_from_object(CeleryConfig)