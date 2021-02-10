from AlchemyEncoder import to_dict
from Utils.TransformUtil import TransformUtil


class ReturnUtil:

    def ok(self, entity=None):
        if entity is None:
            return {}
        # if isinstance(entity, dict):
        #     entity = self._dict_entity(entity)
        return to_dict(entity)

    def notFound(self):
        return

    def falid(self):

        return ""

