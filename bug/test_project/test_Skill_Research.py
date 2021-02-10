from bug.Bug import Animal_Building, BaseInfo, SkillResearch, SkillBuild, World, \
    Animal_mother, Animal_Bug, Research
from bug.TechTree import TechTreeSkill, TechNode, TechNodeBuild

world = World()
# 技术树
tech_tree = TechTreeSkill()
world.set_tech_tree_skill(tech_tree)
tech_tree.set_skill_tech("build", "build")
tech_tree.set_skill_tech("base_research", "node0")

tech1 = TechNode("node0")
tech2 = TechNodeBuild()
tech_tree.add_relation(tech1, tech2)

building_name = "techLab"
info = BaseInfo(building_name, "building")
# 研究院
building = Animal_Building(1)
building.init_info(info)
print(building.skills)
print("[-----------]", building.b_name)

# 设置研究技能
sr1 = SkillResearch(building)
sr1.add_tech_node(tech2)
# sr1.research(1)

building.add_skill(sr1)
building.show_skill_names()
print("-----", building.export_info())
print("building", "[tech_state]", building.skills[1].tech_node.tech_state)

# 添加3只虫子,设置虫子技能 ,验证 解锁是否好使
bug1 = Animal_Bug(1)
sk = SkillBuild(bug1)
bug1.add_skill(sk)

bug2 = Animal_Bug(1)
sk = SkillBuild(bug2)
bug2.add_skill(sk)

bug3 = Animal_Bug(1)
sk = SkillBuild(bug3)
bug3.add_skill(sk)

# 技能未点亮
print("bug1", "techstate", bug1.skills[1].tech_node.tech_state)
print("bug2", "techstate", bug2.skills[1].tech_node.tech_state)
print("bug3", "techstate", bug3.skills[1].tech_node.tech_state)

# 研究解锁
building.show_skill_names()
building.skills[1].set_research_item(1)
building.trigger_skill(1)


# 研究模块
# r=Research()
# r.add_tech_node(tech2)
# r.research(1)

# 结果验证,研究成功,技能可用点亮
print("bug1", "techstate", bug1.skills[1].tech_node.tech_state)
print("bug2", "techstate", bug2.skills[1].tech_node.tech_state)
print("bug3", "techstate", bug3.skills[1].tech_node.tech_state)



