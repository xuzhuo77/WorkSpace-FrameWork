from flask import Flask, render_template, Response
import cv2

# 打开摄像头并灰度化显示
# import cv2 as cv
# 0表示摄像头的编号
# capture = cv.VideoCapture(0)

# while(True):
#     # 获取一帧
#     # 第1个参数ret(return value缩写)是一个布尔值，表示当前这一帧是否获取正确
#     ret, frame = capture.read()
#     # 将这帧转换为灰度图
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break



class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        # url来源见我上一篇博客
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


app = Flask(__name__)


@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = 5000)