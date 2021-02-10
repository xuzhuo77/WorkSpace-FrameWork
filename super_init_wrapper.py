



instance={}
def super_init_wrapper(origin_cls):
    super_class = origin_cls.mro()[1]

    class WrapperClass:
        def __new__(cls, *args, **kwargs):
            if origin_cls not in instance:
                instance[origin_cls] = object.__new__(origin_cls, *args, **kwargs)
                new_instance=instance[origin_cls]
            else:
                new_instance = instance[origin_cls]

            super_class.__init__(new_instance)
            new_instance.__init__(*args, **kwargs)
            return new_instance

    return WrapperClass
