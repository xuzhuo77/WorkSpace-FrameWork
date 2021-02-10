from bug.Log import Log
from SingleInstance import SingleInstance


class Spend():
    money = 0
    population = 0

    def __init__(self, money=0, population=0):
        self.money = money
        self.population = population


class TypeSpend(Spend):
    typename = ""

    def __init__(self, typename="", money=0, population=0):
        super(TypeSpend, self).__init__(money, population)
        self.typename = typename


@SingleInstance
class ResourceTable():
    _dict = {}

    def set_init_data(self, _dict):
        self._dict = _dict

    def add_data(self, name, type_spend):
        self._dict[name] = type_spend

    def find_spends(self, animal_name):
        return self._dict[animal_name]


class NumberManager():
    _number_table = {}

    def __init__(self):
        super(NumberManager, self).__init__()

    def add_number(self, type_spend):
        if type_spend in self._number_table.keys():
            self._number_table[type_spend] += 1
        else:
            self._number_table[type_spend] = 1

    def sub_number(self, type_spend):
        if type_spend in self._number_table.keys():
            if self._number_table[type_spend] - 1 >= 0:
                self._number_table[type_spend] -= 1

    def sum_apend(self):
        spend = Spend()
        for type, number in self._number_table.items():
            spend.money += number * type.money
            spend.population += number * type.population
        return spend


class Resources(NumberManager):
    money = 0
    population = 0

    def __init__(self):
        super(Resources, self).__init__()

    def spend(self, animal_name):
        type_spend = self._can_spend(animal_name)
        if type_spend:
            self.add_number(type_spend)

    def _can_spend(self, animal_name):
        spends = self._find_spend(animal_name)
        rest_reource = self.rest_resource()
        if rest_reource.money - spends.money < 0:
            Log.show("mongy 不足")
            return False
        elif rest_reource.population - spends.population < 0:
            Log.show("population 不足")
            return False
        else:
            return spends

    def _find_spend(self, animal_name):
        return ResourceTable().find_spends(animal_name)

    def add_resources(self, animal_name):
        spend = ResourceTable().find_spends(animal_name)
        self.money += spend.money
        self.population += spend.population

    def sub_resources(self, animal_name):
        spend = ResourceTable().find_spends(animal_name)
        self.money += spend.money
        self.population += spend.population

    def rest_resource(self):
        spends = self.sum_apend()
        return Spend(self.money - spends.money, self.population - spends.population)
