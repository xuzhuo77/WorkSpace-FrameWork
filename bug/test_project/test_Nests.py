from bug.Bug import Animal_Egg
from bug.Nest import NestAnimal

nest=NestAnimal(1)

# nest add egg
egg=Animal_Egg(1)
nest.add_egg(egg)
print(nest.egg)
print(nest.has_egg())

#已满
egg2=Animal_Egg(1)
nest.add_egg(egg2)


# 删除egg
nest.remove_egg()
print(nest.egg)
print(nest.has_egg())


