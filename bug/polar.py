import numpy as np


def polar_2_rectangular(r_theta):
    r_theta = np.array(r_theta)
    theta = r_theta[:, 1].reshape(r_theta.shape[0], 1)
    r = r_theta[:, 0].reshape(r_theta.shape[0], 1)
    return r * np.hstack([np.cos(theta), np.sin(theta)])


# test_polar_2_retangular
r_theta = [[2, np.pi], [3, np.pi / 2], [1, np.pi * 2]]
print(polar_2_rectangular(r_theta))
for rt in r_theta:
    print([rt[0] * np.cos(rt[1]), rt[0] * np.sin(rt[1])])

print(np.array([[1], [2]]) * np.array([[3], [4]]))


def old_PolarRect(r, rw, theta, thetah):
    return [[r, theta], [r + rw, theta], [r + rw, theta + thetah / 2], [r + rw, theta + thetah], [r, theta + thetah],
            [r, theta + thetah / 2], [r, theta]]


# r,rw,theta,thetah
def PolarRect(r, rw, theta, thetah):
    n = 7
    t = np.zeros([n * 2 + 3, 2])
    t[0] = [r, theta]
    t[n + 1] = [r + rw, theta + thetah]
    per_th = thetah / n
    for i in range(n):
        t[1 + i] = [r + rw, theta + per_th * i]
        t[n + 2 + i] = [r, theta + thetah - per_th * i]
    t[n * 2 + 2] = [r, theta]
    return t


def path_moveto(path):
    len = path.shape[0]
    t = [Path.LINETO for i in range(len - 2)]
    t.insert(len - 1, Path.CLOSEPOLY, )
    t.insert(0, Path.MOVETO)
    return t

def rect_2_patches(rect):
    rectangular = polar_2_rectangular(rect)
    codes = path_moveto(rectangular)
    path2 = Path(rectangular, codes)
    patch2 = patches.PathPatch(path2, facecolor='orange', lw=2)
    return patch2


# test polarRect
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
rect = PolarRect(1, 2, np.pi / 8, np.pi / 6)
rectangular1 = polar_2_rectangular(rect)
codes = path_moveto(rectangular1)
path = Path(rectangular1, codes)
patch = patches.PathPatch(path,  lw=2)

rect = PolarRect(1, 1, np.pi / 8+np.pi/9, np.pi / 8)
patch2=rect_2_patches(rect)

rect = PolarRect(1, 1, np.pi / 8, np.pi / 8)
patch3=rect_2_patches(rect)

rect = PolarRect(3, 1, np.pi / 12, np.pi / 8)
patch4=rect_2_patches(rect)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-0, 8)
ax.set_ylim(-0, 8)

ax.add_patch(patch)
ax.add_patch(patch2)
ax.add_patch(patch3)
ax.add_patch(patch4)

rect = PolarRect(6, 0.3, np.pi / 4, np.pi / 12)
patch4=rect_2_patches(rect)
ax.add_patch(patch4)

plt.show()


