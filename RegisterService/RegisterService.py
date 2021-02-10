from RegisterService.Registration import Registration
from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic


@super_init_wrapper
class RegisterService(ServiceBasic):
    __eneity__ = Registration



