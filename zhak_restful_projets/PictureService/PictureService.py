from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic
from zhak_restful_projets.PictureService.Picture import Picture


@super_init_wrapper
class PictureService(ServiceBasic):
    __eneity__ = Picture


