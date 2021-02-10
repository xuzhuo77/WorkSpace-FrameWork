

from bug.Bug import Animal_Egg,World
from bug.Nest import NestAnimal

egg = Animal_Egg(None)
nest=NestAnimal(1)

world=World()
world.add_animal(egg)
world.add_animal(nest)
nest.add_egg(egg)
egg.trigger_skill(1)
print(World().animal_list)
world.update()
world.update()
print(World().animal_list)

world.update()
world.update()
# world.update()
print(World().animal_list)
print(nest.has_egg())







