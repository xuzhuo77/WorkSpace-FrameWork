from bug.Log import Log
from bug.Bug import Animal_Nest,Animal_Egg


class Nest():
    egg = None

    def __init__(self):
        pass

    def has_egg(self):
        return True if self.egg else False

    def add_egg(self, egg):
        if not self.has_egg():
            self.egg = egg
            egg.set_nest(self)
        else:
            Log.show("已满")

    def remove_egg(self):
        if self.has_egg():
            egg = self.egg
            self.egg = None
            return egg
        return None


class NestAnimal(Animal_Nest, Nest):
    def __init__(self, camp):
        super(NestAnimal, self).__init__(camp=camp)


class EggBuilding(Animal_Egg):
    def __init__(self, camp):
        super(EggBuilding, self).__init__(camp=camp)



