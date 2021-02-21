import time


def mktime(datetime_parm):
    return int(time.mktime(time.strptime(str(datetime_parm), "%Y%m%d")))
