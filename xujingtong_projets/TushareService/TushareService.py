from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic
from xujingtong_projets.TushareService.Tushare import Tushare


@super_init_wrapper
class TushareService(ServiceBasic):
    __eneity__ = Tushare



