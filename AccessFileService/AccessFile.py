from Entity import Entity
from sqlalchemy import String, Column


class AccessFile(Entity):
    __tablename__ = 'f_accessfle'

    parent_guid= Column(String(64))
    module_name=Column(String(128))
    file_path=Column(String(128))
    service_filename=Column(String(128))
    token=Column(String(256))
    upload_filename=Column(String(128))
    # size=Column(String(64))

    def saveFile(self):
        pass






