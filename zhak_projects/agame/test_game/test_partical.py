import numpy as np

from zhak_projects.agame.elements.weapon import ParticalSystem, Bullet


def test_partical():
    n_rows=100
    width,height=16,16
    particals=np.random.randint(4,9,(n_rows,3))
    particals=np.column_stack((particals, np.zeros(n_rows)))
    # move
    # update
    destination=np.array([10,10])
    print(destination - particals[:,:2])
    particals_show=particals[np.argwhere(np.linalg.norm((destination - particals[:,:2]), axis=1, keepdims=True)>1)[:,0]]



    # expand
    # particals=particals+np.column_stack((particals_move,np.zeros((n_rows,2))))
    rect=np.column_stack((particals_show[:,0:2],np.repeat(np.array([[width,height]]),particals_show.shape[0],axis=0)))
    # rect=np.column_stack((np.ones(rect.shape[0]),rect))
    rect=[(1,t) for t in rect.tolist()]
    print(rect)


test_partical()



# import pygame
# surface=pygame.Surface((1,2))
#
# bullet=Bullet()
# bullet.image=surface
# bullet.switcher=True
# for t in range(30):
#     bullet.update()
#     # print(bullet.particals)
#     bullet.draw()