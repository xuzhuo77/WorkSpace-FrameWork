from flask import Blueprint

from Utils.ReturnUtil import ReturnUtil
from xujingtong_projets.TushareService.TushareService import TushareService
from flask_apscheduler import APScheduler
scheduler = APScheduler()

class SchedulerConfigTushare(object):
    JOBS = [ ]
def task1(a, b):
    print(str(a) + ' ' + str(b))

TushareBluePrint = Blueprint("tushare", __name__)
tushare_service=TushareService()

@TushareBluePrint.route('/number', methods=["Get"])
def number():
    return ReturnUtil().ok(tushare_service.find_list())

@TushareBluePrint.route('/addjob',methods=['GET','POST'])
def addtask():
    scheduler.add_job(func=task1, id='1', args=(1, 2), trigger='interval', seconds=5, replace_existing=True)
    return 'sucess'



