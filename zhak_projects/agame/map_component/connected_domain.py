class ConnectedDomainMap():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def showMap(self):
        for row in self.map:
            s = ''
            for entry in row:
                if entry == 0:
                    s += '..'
                elif entry == 1:
                    s += ' #'
                elif entry == 2:
                    s += ' &'
                elif entry == 3:
                    s += ' T'
                else:
                    s += ' X'
            print(s)


# map=ConnectedDomainMap(20,10)
# map.showMap()

def choice(nextv,sideW,sideH,arealist):

    d = np.argwhere((nextv[:, 1] < sideW) & (nextv[:, 1] > -1) & (nextv[:, 0] < sideH) & (nextv[:, 0] > -1)&
                    np.array([(nextv[0] != arealist).any(1).all(), (nextv[1] != arealist).any(1).all(),
                              (nextv[2] != arealist).any(1).all(), (nextv[3] != arealist).any(1).all()]))
    np.random.shuffle(d)
    return nextv[d[0]]

import numpy as np
def random_patch(area,type,size,map,area_list=None):
    area =area
    size=size
    startPoint = np.random.randint(0, size, size=(2))
    map[startPoint[0], startPoint[1]] = 1
    if  area_list is None:
        area_list=np.array([startPoint])
    currentPoint = startPoint
    area-=1
    while area > 0:
        choiced = currentPoint + np.array([[1,0],[-1,0],[0,1],[0,-1]])
        try:
            currentPoint=choice(choiced,size,size,area_list)
        except:

            # 异常:走投无路,重新选新起点
                newstart = np.argwhere(map == 0)
                np.random.shuffle(newstart)
                currentPoint = np.atleast_2d(newstart[0])



        # if not (currentPoint==arealist).all(1).any():
        #     currentPoint = currentPoint + np.array([[1,0],[-1,0],[0,1],[0,-1]])[np.random.randint(0,4)]



        area_list=np.vstack((area_list,currentPoint))
        map[currentPoint[0][0], currentPoint[0][1]] = type
        area -= 1
    return map ,area_list


def MapGenerate(size=30,area=200):
    map = np.zeros((size, size))
    map,area_list=random_patch(area,1,size,map)
    map,area_list=random_patch(area,2,size,map,area_list)
    map,area_list=random_patch(area,3,size,map,area_list)
    # map,area_list=random_patch(area,4,size,map,area_list)
    map[:, [0, -1]] = 0
    map[[0, -1]] = 0
    return map




if __name__ == '__main__':
    print(map)
    c = ConnectedDomainMap(20, 10)
    c.map = MapGenerate()
    c.showMap()