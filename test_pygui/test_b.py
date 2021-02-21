from dearpygui.core import *
from dearpygui.simple import *
from time import sleep
import threading

add_additional_font(file='C:\\Windows\\Fonts\\simhei.ttf', size=18.0, glyph_ranges='chinese_simplified_common')


def long_async_preparer(sender, data):
    floaty = get_value("异步输入数据")
    thread_floaty = threading.Thread(target=long_callback, args=(1, log_debug, floaty,))
    thread_floaty.start()
    # run_async_function(long_callback, floaty, return_handler=long_async_return)


def long_callback(sender, callback, data):
    sleep(3)
    data = data * 2
    callback(data)
    return data


def long_async_return(sender, data):
    log_debug(data)


def long_callback2(sender, data):
    sleep(3)
    log_debug(data * 2)


show_logger()

with window("Tutorial"):
    add_text("输入一个数字，然后在logger窗口中查看回调的输出，该回调通常会使整个GUI冻结")
    add_input_float("异步输入数据", default_value=4.0)
    # add_button("耗时方法", callback=long_callback2, callback_data=get_value("异步输入数据"),
    #            tip="This is the long callback that will freeze the gui")
    add_button("耗时异步方法", callback=long_async_preparer, tip="this will not a freeze the GUI")

start_dearpygui()
