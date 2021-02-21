import time
import cv2 as cv

import queue  # 队列模块


def produce_frame():
    global frame
    capture = cv.VideoCapture(0)
    while capture.isOpened():

        ret, frame = capture.read()
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        yield frame
        # return frame
        if cv.waitKey(30) == ord('q'):
            break
        consume_frame()

    # for i in range(1,21):
    #     time.sleep(1)
    #     yield i
    #     print("第%s个包子做好了"%i)
    #     consume_baozi()


def consume_frame():
    global frame
    # time.sleep(1)
    # print("第%s个人吃了第%s个包子"%(i,i))
    cv.imshow('frame', frame)


def run():
    res = produce_frame()
    while True:
        try:
            res.__next__()
        except StopIteration:
            break
