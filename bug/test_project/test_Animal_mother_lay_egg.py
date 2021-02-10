from bug.Bug import World, Animal_mother

w = World()
mother = Animal_mother(1,)
w.add_animal(mother)

# build
mother.trigger_skill(2)
w.update()
print(w.animal_list,mother.camp)

#lay

mother.trigger_skill(1)
print(w.animal_list)
w.update()
w.update()
w.update()
w.update()



print(w.animal_list)