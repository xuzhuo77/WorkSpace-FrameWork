from multiprocessing import Lock

instance = {}


def SingleInstance(cls):
    cls.__lock__ = Lock()

    def new(cls, *args, **kwargs):
        cls.__lock__.acquire()

        try:
            if cls not in instance:
                instance[cls] = object.__new__(cls)
            return instance[cls]
        finally:
            cls.__lock__.release()

    cls.__new__ = new
    return cls
