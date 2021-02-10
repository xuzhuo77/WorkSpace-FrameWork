from zhak_projects.agame.elements.Ghost import Kuaile
from zhak_projects.agame.elements.Panels import Panel
from zhak_projects.agame.zhgame import is_in_rect

import numpy as np
panel=Panel()
x,y=2,3
print("mouse click in Panel Range",is_in_rect(np.array([x,y]), panel.pos, panel.width_height))


# 连接 sprite
# 点击sprite后,更新panel 显示sprite的信息
sa=Kuaile()
sa.pos=np.random.randint(-100,100, size=(1,2))
sa.name="KuaileTest"

panel.update_content(sa)
print(panel.content)
