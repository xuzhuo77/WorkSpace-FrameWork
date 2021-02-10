import numpy as np


sideW=50
sideH=30





next=np.array([[-1,0],[1,0],[0,-1],[0,1]])


nextv=np.array([25,49])+next
nextv1=np.array([29,38])+next

print((nextv[:,1]<sideW))
print((nextv[:,1]>-1))

print(nextv1[:,0]<sideH)
print(nextv1[:,0]>-1)
print(2,(nextv[:,1]<sideW)&(nextv[:,1]>-1)&(nextv1[:,0]<sideH)&(nextv1[:,0]>-1))

nextv=np.array([25,0])+next
nextv1=np.array([0,38])+next

print((nextv[:,1]<sideW))
print((nextv[:,1]>-1))
print((nextv1[:,0]<sideH))
print((nextv1[:,0]>-1))
choice=np.random.randint(0,4)

print(2,(nextv[:,1]<sideW)&(nextv[:,1]>-1)&(nextv[:,0]<sideH)&(nextv[:,0]>-1))
d=np.argwhere((nextv[:,1]<sideW)&(nextv[:,1]>-1)&(nextv[:,0]<sideH)&(nextv[:,0]>-1))
np.random.shuffle(d)
print(d,nextv[d[0]])

print(next[choice])

def choice(nextv,sideW,sideH):
    d = np.argwhere((nextv[:, 1] < sideW) & (nextv[:, 1] > -1) & (nextv[:, 0] < sideH) & (nextv[:, 0] > -1))
    np.random.shuffle(d)
    return nextv[d[0]]