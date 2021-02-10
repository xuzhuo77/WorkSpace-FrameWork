from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic
from zhak_restful_projets.AccessoryFileService.AccesssoryFile import AccessoryFile


@super_init_wrapper
class AccessoryFileService(ServiceBasic):
    __eneity__ = AccessoryFile



