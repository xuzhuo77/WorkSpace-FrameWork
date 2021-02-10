from AccessFileService.AccessFile import AccessFile
from Utils.AccessFileUtil import FlaskAccessFileUtil
from super_init_wrapper import super_init_wrapper
from ServiceBasic import ServiceBasic


@super_init_wrapper
class AccessFileService(ServiceBasic):
    __eneity__ = AccessFile

    def save_file(self, requestfile, fileParam=None):
        util = FlaskAccessFileUtil()

        result = util.api_upload(requestfile, fileParam)
        access = AccessFile(guid=fileParam.guid, module_name=fileParam.module_name,
                            token=result["token"])
        self.create(access)
        return result

    def download(self, guid):
            accessfile = self.find_by_guid(guid)
            f = FlaskAccessFileUtil()
            return f.download(accessfile)
            # return file
