from super_init_wrapper import super_init_wrapper
from FirstService.First import First
from ServiceBasic import ServiceBasic


@super_init_wrapper
class FirstService(ServiceBasic):
    __eneity__ = First


# f=FirstService()
