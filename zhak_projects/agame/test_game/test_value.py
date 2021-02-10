from zhak_projects.agame.zhgame import Actor

name=["guofeng","xuzhuo","mengfanjie","lihongxin","zhangyan","xujingtong"]
attack=[5,2,1,4,5,9]
hp=[50,30,40,20,18,22]
defance=[2,1,4,5,1,3]
speed=[2,1,1,1,2,3]
rate=[0.2,0.2,0.2,0.2,0.2,0.2]
lucky=[0,0,0,0,0,0]
attack_range=[10,10,10,10,10,10]
token=["诶我操了..","我冷..","我跟你讲...","干你好啊..","这又触及到我知识盲区了..","我太难了.."]


def init_actor_list():
    actor_list = []
    for k,init_actor in enumerate(zip(name,attack,hp,defance,speed,rate,lucky,attack_range)):
        init_actor=(k,init_actor[0],init_actor[1],init_actor[2],init_actor[3],init_actor[4],init_actor[5],init_actor[6],init_actor[7])
        actor_list.append(Actor(*init_actor))
    return actor_list

delete_list=[]
