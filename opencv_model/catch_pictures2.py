import cv2
import numpy as np
from PIL import Image
import os
# from opencv_model.OpencRead import read_content
folder = "" # 拍照文件目录
counter = 0

class  CameraRun():
    counter=0
    def shot(self,pos, frame):
        path = pos.upper() +os.sep+ pos + "" + str(self.counter) + ".BMP"

        cv2.imwrite(path, frame)
        print("snapshot saved into: " + path)
    def runCamera(self):
        cap = cv2.VideoCapture(0)
        # ret = cap.set(3, 320)
        # ret = cap.set(4, 240)
        # 设置摄像头分辨率
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        i = 0

        while cap.isOpened():
            ret, frame = cap.read()
            left_img = frame[:, 0:640, :]
            right_img = frame[:, 640:1280, :]
            if ret:
                # 显示两幅图片合成的图片
                # cv2.imshow('img', frame)
                # 显示左摄像头视图
                cv2.imshow('left', left_img)

                # image = Image.fromarray(cv2.cvtColor(left_img, cv2.COLOR_BGR2RGB))
                # read_content(image)
                # 显示右摄像头视图
                cv2.imshow('right', right_img)
            key = cv2.waitKey(delay=2)
            if key == ord('t'):
                cv2.imwrite('./img/test' + str(i) + '.jpg', frame)  #
                i += 1
            if key == ord("q") or key == 27:
                break
            elif key == ord("s"):
                self.shot("left", left_img)
                self.shot("right", right_img)
                self.counter += 1

        cap.release()
        cv2.destroyAllWindows()

cr=CameraRun()
cr.runCamera()