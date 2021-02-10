import sys
sys.path.append('..')
from ServiceDocNewCheckPlan.DocNewCheckPlan import DocNewCheckPlan
from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic


# @super_init_wrapper
class DocNewCheckPlanService(ServiceBasic):
    __eneity__ = DocNewCheckPlan
    name = "docnewcheckplan_service"


# f=DocNewCheckPlanService()
# print(f.find_list())