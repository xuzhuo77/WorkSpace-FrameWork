from PIL import Image
import os
img = Image.open(os.getcwd()+os.sep+"insect2.png")

# 旋转方式一
img1 = img.transpose(Image.ROTATE_180)   # 引用固定的常量值
img1.save("insect2.png")

# 旋转方式二
# img2 = img.rotate(180)   # 自定义旋转度数
# img2 = img2.resize((400, 400))   # 改变图片尺寸
# img2.save("r2.png")