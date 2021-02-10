from bug.Bug import Animal_mother, World
from bug.UI import UI, Panel, Button

ui = UI()
world = World()
mother = Animal_mother(1, )
world.add_animal(mother)
mother.show_skill_names()

mother_panel = Panel()
b1 = Button()
b1.name = "layEgg"
b2 = Button()
b2.name = "build"
mother_panel.set_skill(b1)
mother_panel.set_skill(b2)

mother_panel.set_target(mother)

mother_panel.trigger(b1)

print(mother_panel.return_skills())
