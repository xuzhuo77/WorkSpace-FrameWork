import uuid


def gen_id():
    return uuid.uuid4().hex


def gen_guid():
    typ = [10, 6, 2, 4, 2, 8]
    sumstr = ""
    str = uuid.uuid4().hex
    for i in range(len(typ) - 1):
        sumstr += str[typ[i]:typ[i] + typ[i + 1]] + "-"
    sumstr += str[typ[-2]:typ[-2] + typ[-2 + 1]]
    return sumstr
