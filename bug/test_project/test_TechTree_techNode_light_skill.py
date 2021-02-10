from bug.Bug import World, Animal_mother
from bug.TechTree import TechTree, TechNodeLayEgg, TechNodeBuild, TechTreeSkill, TechNode

world = World()
tech_tree = TechTreeSkill()
world.set_tech_tree_skill(tech_tree)

tech_tree.set_skill_tech("build", "build")
tech_tree.set_skill_tech("layEgg", "layEgg")

print(id(tech_tree))
t1 = TechNode("skill_base")
t2 = TechNodeBuild()
t3 = TechNodeLayEgg()


tech_tree.add_relation(t1, t2)
tech_tree.add_relation(t2, t3)
print(tech_tree.edges())

mother = Animal_mother(camp=1, )
world.add_animal(mother)

# not allow to build
mother.trigger_skill(2)
print("edges2",tech_tree.edges())
print("not allow to build", world.animal_list)


tech_tree.ligth_node(t1)
tech_tree.ligth_node(t2)
tech_tree.show_state()


# allow to build
mother.trigger_skill(2)
print("allow to build", world.animal_list)
