import cv2
import time

AUTO = True  # 自动拍照，或手动按s键拍照
INTERVAL = 2 # 自动拍照间隔

cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 400, 0)
left_camera = cv2.VideoCapture(0)
right_camera = cv2.VideoCapture(1)

counter = 0
utc = time.time()
pattern = (12, 8) # 棋盘格尺寸
folder = "./snapshot/" # 拍照文件目录

def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"

    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)

while left_camera.isOpened():

    ret1, left_frame = left_camera.read()
    if ret1:
        cv2.imshow("left", left_frame)

    ret2, right_frame = right_camera.read()
    if ret2:
        cv2.imshow("right", right_frame)

    if ret1 and ret2:
        now = time.time()
        if AUTO and now - utc >= INTERVAL:
            shot("left", left_frame)
            shot("right", right_frame)
            counter += 1
            utc = now

    key = cv2.waitKey(2)
    if key == ord("q"):
        # pass
        break
    elif key == ord("s"):
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1

left_camera.release()
right_camera.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")
