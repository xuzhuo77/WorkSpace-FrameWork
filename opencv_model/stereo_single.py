import cv2
import numpy as np
import glob



board_size = [7,7]
impoints=[]
l_impoints=[]
r_impoints=[]
objpoints=[]
objp = np.zeros((board_size[0]* board_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)
idx=1
a=cv2.imread("LEFT/left{}.bmp".format(str(idx)))
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(a, (board_size[0], board_size[1]), None)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
conners2=cv2.cornerSubPix(b,corners,(11,11),(-1,-1),criteria)
cv2.drawChessboardCorners(a,(board_size[0], board_size[1]),conners2,True)
cv2.namedWindow("winname",cv2.WINDOW_NORMAL)
cv2.imshow("winname",a)
cv2.waitKey(0)
l_impoints.append(conners2)

a=cv2.imread("Right/right{}.bmp".format(str(idx)))
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(a, (board_size[0], board_size[1]), None)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
conners2=cv2.cornerSubPix(b,corners,(11,11),(-1,-1),criteria)
cv2.drawChessboardCorners(a,(board_size[0], board_size[1]),conners2,True)
cv2.namedWindow("winname",cv2.WINDOW_NORMAL)
cv2.imshow("winname",a)
cv2.waitKey(0)

img_shape = b.shape[::-1]
r_impoints.append(conners2)
impoints.append(conners2)
objpoints.append(objp)
rt, M1, d1, r1, t1 = cv2.calibrateCamera( objpoints, l_impoints, img_shape, None, None)
rt, M2, d2, r2, t2 = cv2.calibrateCamera( objpoints, r_impoints, img_shape, None, None)

print(M1)
print(M2)

flags = 0
flags |= cv2.CALIB_FIX_INTRINSIC
# flags |= cv2.CALIB_FIX_PRINCIPAL_POINT
flags |= cv2.CALIB_USE_INTRINSIC_GUESS
flags |= cv2.CALIB_FIX_FOCAL_LENGTH
# flags |= cv2.CALIB_FIX_ASPECT_RATIO
flags |= cv2.CALIB_ZERO_TANGENT_DIST
stereocalib_criteria = (cv2.TERM_CRITERIA_MAX_ITER +cv2.TERM_CRITERIA_EPS, 100, 1e-5)
ret, M1, d1, M2, d2, R, T, E, F = cv2.stereoCalibrate(objpoints, l_impoints,r_impoints, M1,d1, M2,d2, img_shape,criteria=stereocalib_criteria, flags=flags)

print('Intrinsic_mtx_1', M1)
print('dist_1', d1)
print('Intrinsic_mtx_2', M2)
print('dist_2', d2)
print('R', R)
print('T', T)
print('E', E)
print('F', F)

camera_model = dict([('M1', M1), ('M2', M2), ('dist1', d1),
                     ('dist2', d2), ('rvecs1', r1),
                     ('rvecs2', r2), ('R', R), ('T', T),
                     ('E', E), ('F', F)])
print(camera_model)