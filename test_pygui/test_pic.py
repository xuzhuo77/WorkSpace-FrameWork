import dearpygui.core as dpg
import dearpygui.simple as sdpg
import dearpygui.demo as do

from PIL import ImageGrab
from PIL import Image
import time
import threading
import cv2 as cv
import numpy as np
global running
running=False
def produce_frame():
    global frame
    global running
    capture = cv.VideoCapture(0)
    running=True
    while capture.isOpened() and running:
        time.sleep(0.1)
        ret, frame = capture.read()
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img =frame
        b = np.ones([img.shape[0], img.shape[1], 1]) * 255
        img = np.c_[img, b].astype(int)
        dpg_image2 = img.flatten().tolist()
        dpg.add_texture("texture id", dpg_image2, img.shape[1], img.shape[0])
        dpg.draw_image('drawing', "texture id", [0, 0], [500, 300])
        # return frame
        if cv.waitKey(30) == ord('q'):
            break


global thread_floaty
thread_floaty=None

def camera_frame_control():
    global thread_floaty
    global running
    if not thread_floaty:
        dpg.log_debug("start")
        thread_floaty = threading.Thread(target=produce_frame, args=())
        thread_floaty.setDaemon(True)
        thread_floaty.start()
        print(id(thread_floaty))

    else:
        print(id(thread_floaty))
        running=False
        thread_floaty.join()
        dpg.log_debug("stop")
        thread_floaty = None
    with sdpg.window():
        dpg.add_drawing('drawing', width=1000, height=800)
        dpg.add_text("tooltipTest")


with sdpg.window("Main Window"):
    # dpg.set_main_window_size(1400, 800)
    dpg.set_main_window_title("Pixel selector")
    # dpg.add_
    dpg.add_button("camera##1", callback=camera_frame_control, tip="this will not a freeze the GUI")





dpg.show_logger()
do.show_demo ()
dpg.start_dearpygui()
