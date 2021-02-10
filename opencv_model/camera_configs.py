import cv2
import numpy as np

# 左摄像头参数
# left_camera_matrix = np.array([[1394.26663, 0, 343.36581],
#                                [0, 1393.25572, 206.56092],
#                                [0, 0, 1]])
# left_distortion = np.array([[-0.66451, 0.84137, -0.01001, -0.00274, 0]])
#
# # 右摄像头参数
# right_camera_matrix = np.array([[1385.46346, 0, 344.38903],
#                                 [0, 1385.09596, 197.18927],
#                                 [0, 0, 1]])
# right_distortion = np.array([[-0.63339, -0.68796, -0.00491, -0.00675, 0]])
#
# om = np.array([0.00456, 0.01463, 0.00042])  # 旋转关系向量
# R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-59.63351, -0.15514, -0.35781])  # 平移关系向量
print(T.shape)
# # T = np.array([0,0,0])  # 平移关系向量

import pickle
with open("name.txt","rb") as f:
    r=pickle.load(f)


left_camera_matrix=r["M1"]
left_distortion=r["dist1"]
right_camera_matrix=r["M2"]
right_distortion=r["dist2"]
R=r["R"]
print(r["T"].shape)
T=r["T"]







# size = (640, 360)
size = (640,480)
# 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
