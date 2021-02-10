from SingleInstance import SingleInstance

from bug.Log import Log
from bug.Timer import Timer, TimerColdDown, TimerInterval


class Skill():
    def __init__(self, skill_name, colddown_time, parent):
        self.skill_name = skill_name
        self.colddown_time = TimerInterval(colddown_time)
        self.parent = parent
        self.tech_node = None
        techtreeskill = World().get_tech_tree_skill()
        if techtreeskill:
            self.set_tech_node(techtreeskill.get_node_by_skill_name(self.skill_name))

    def set_tech_node(self, tech_node):
        self.tech_node = tech_node

    def trigger(self):
        # tech_can_use=None
        # if self.tech_node:
        #     tech_can_use=self.tech_node.can_use()
        # if  tech_can_use:
        cold_donn = TimerColdDown().finish(self.colddown_time)
        Log().show(self.skill_name + " coldown " + str(cold_donn))
        if cold_donn is True:
            Log().show("trigger:" + self.skill_name)
            TimerColdDown().trigger(self.colddown_time)
            self.activate_trigger()

    def update(self):
        if not TimerColdDown().finish(self.colddown_time):
            self.activate_update()

    def activate_update(self):
        print(self.skill_name)

    def activate_trigger(self):
        pass


class Skills():
    def __init__(self):
        self.skills = {}
        self.parent = None

    def add_skill(self, skill):
        self.skills[len(self.skills) + 1] = skill

    def trigger_skill(self, i):
        self.skills[i].trigger()

    def skills_update(self):
        for skill in self.skills.values():
            skill.update()

    def _dict_skills(self):
        skills = {str(k) + ":" + sk.skill_name for k, sk in self.skills.items()}
        return skills

    def show_skill_names(self):
        Log.show("SKILLS:" + " ".join(self._dict_skills()))


class Camp():
    def __init__(self, camp):
        self.camp = camp


# class sysResource():
#     _resource = {}
#
#     def find_resource(self, res_name):
#         return self._resource[res_name]
#
#     def save_resource(self, _name, resource):
#         self._resource[_name] = resource


class BaseInfo():
    b_name = None
    b_version = 1
    b_type = None

    def __init__(self, b_name=None, b_type=None):
        self.b_name = b_name
        self.b_version = 1
        self.b_type = b_type

    def init_info(self, baseInfo):
        self.b_name = baseInfo.b_name
        self.b_type = baseInfo.b_type

    def export_info(self):
        return {"name": self.b_name, "skills": self._dict_skills()}


class Animal(Skills, Camp, BaseInfo):
    def __init__(self, camp, ):
        super(Animal, self).__init__()
        Camp.__init__(self, camp)

    def update(self):
        self.skills_update()


class Animal_mother(Animal):
    def __init__(self, camp):
        super(Animal_mother, self).__init__(camp=camp)
        skill1 = SkillLayEgg(self)
        skill1.set_prototype(Animal_Egg)
        self.add_skill(skill1)
        skill2 = SkillBuild(self)
        skill2.set_prototype(Animal_Nest)
        self.add_skill(skill2)


class Animal_Egg(Animal):
    def __init__(self, camp):
        super(Animal_Egg, self).__init__(camp)
        x = SKillHatch(self)
        self.add_skill(x)
        x.trigger()
        self.nest = None

    def set_nest(self, nest):
        self.nest = nest


class Animal_Bug(Animal):
    def __init__(self, camp):
        super(Animal_Bug, self).__init__(camp)


class Animal_Nest(Animal):
    def __init__(self, camp):
        super(Animal_Nest, self).__init__(camp)


class Animal_Building(Animal):
    def __init__(self, camp):
        super(Animal_Building, self).__init__(camp=camp)


class Creator():
    _prototype = None

    def set_prototype(self, prototype):
        self._prototype = prototype

    def creatInstance(self, args):
        pro = self._prototype(args)
        return pro


class CreatorBuilding(Creator):
    pass


class SkillBuild(Skill, CreatorBuilding):
    def __init__(self, parent):
        super(SkillBuild, self).__init__("build", 8, parent)

    def activate_trigger(self):
        ins = self.creatInstance(self.parent.camp)
        World().add_animal(ins)


class Research():
    _ready_to_research = {}

    def add_tech_node(self, tech_node):
        self._ready_to_research[len(self._ready_to_research) + 1] = tech_node

    def research(self, i):
        self._ready_to_research[i].light_node()


class SkillResearch(Skill, Research):
    def __init__(self, parent):
        super(SkillResearch, self).__init__("base_research", 3, parent)
        self.research_item = 0

    def activate_trigger(self):
        # 在研究结束的时候触发点亮技能节点
        self.research(self.research_item)
        self.research_item=0
        Log().show("  research light skill")

    def set_research_item(self, i):
        self.research_item = i


class CreatorLayEgg(Creator):
    pass


class SkillLayEgg(Skill, CreatorLayEgg):
    def __init__(self, parent):
        super(SkillLayEgg, self).__init__("layEgg", 4, parent)

    def activate_trigger(self):
        ins = self.creatInstance(self.parent.camp)
        World().add_animal(ins)


@SingleInstance
class DelayTimer(Timer):
    pass


class SKillHatch(Skill):
    def __init__(self, egg):
        super(SKillHatch, self).__init__("SKillHatch", 9, egg)
        self.hatch_Time = TimerInterval(self.colddown_time.interval - 1)

    def trigger(self):
        TimerColdDown().trigger(self.hatch_Time)

    def update(self):
        delaytime = TimerColdDown().finish(self.hatch_Time)
        if delaytime <= 0:
            self.update_trigger()

    def update_trigger(self):
        World().add_animal(Animal_Bug(1))
        egg = self.parent
        World().remove_animal(egg)
        if egg.nest:
            egg.nest.remove_egg()

    def activate_trigger(self):
        Log().show(self.skill_name)


class AnimalList():
    animal_list = []

    def __init__(self):
        pass

    def add_animal(self, animal):
        self.animal_list.append(animal)

    def animals_update(self):
        for ani in self.animal_list:
            ani.update()

    def remove_animal(self, animal):
        self.animal_list.remove(animal)


@SingleInstance
class World(AnimalList):
    tech_tree_skill = None

    def get_tech_tree_skill(self):
        return self.tech_tree_skill

    def set_tech_tree_skill(self, tech_tree):
        self.tech_tree_skill = tech_tree

    def update(self):
        AnimalList.animals_update(self)
        TimerColdDown().update()
