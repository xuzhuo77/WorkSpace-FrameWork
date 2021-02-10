from zhak_projects.agame.test_game.test_actor import init_actor_list
from zhak_projects.agame.test_game.test_value import delete_list
from zhak_projects.agame.zhgame import delete_actor, delete_actor_actor_list

actor_list=init_actor_list()



print(delete_list)
delete_actor(actor_list[0])
print(delete_list)
delete_actor_actor_list(delete_list,actor_list)
print(actor_list,)

