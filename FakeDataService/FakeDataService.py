from DataBase.SqlEngine import oracle_Engine, url_path, mysql_engine
from FakeDataService.FakeData import FakeData
from Utils.AutomapUtil import generateMappedEneity, generateService
from Utils.FakerUtil import FakerUtil
from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic


@super_init_wrapper
class FakeDataService(ServiceBasic):
    __eneity__ = FakeData

    def profile(self):
        f = FakeData()
        f.contentValue = FakerUtil().profile()
        return f

    def add_randomvalue_by_entity(self):
        engine = mysql_engine(url_path["myself"])
        table_name = "z_docnewcheckplan"
        mapped_entity = generateMappedEneity(engine, table_name)

        # list = generateService(mapped_eneity)().find_list()
        # print(list)

        a = FakerUtil().entity_fake_data(mapped_entity)
        fake_service = generateService(mapped_entity)()
        result = fake_service.create(a)
        return result
