from zhak_projects.agame.map import ViewPort
import numpy as np

from zhak_projects.agame.zhgame import sprite_shake

view_port=ViewPort()
view_port.pos=np.array([50,50])
print("world point",view_port.to_world(np.array([44.3,50])))
print("world point",view_port.to_world(np.array([44.3,50])))
view_port.pos=np.array([-10,50])
print("world point",view_port.to_world(np.array([-44.3,-150])))

print(view_port.pos)
sprite_shake(view_port)
print(view_port.pos)

for  i in range(100):
    print(np.random.randint(-1,2,size=(1,2))*2)