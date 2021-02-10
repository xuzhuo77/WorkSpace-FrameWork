from PIL import Image
import os
bath_path='D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\'
# bath_path='E:\\pythonWebWorkSpace\\zhak_projects\\agame\\statics\\'
filename = 'light.gif'

# 使用Image模块的open()方法打开gif动态图像时，默认是第一帧
im = Image.open(bath_path+filename)
# 文件夹名字，可以随意取
pngDir = filename[:-4]

# 创建存放每帧图片的文件夹
if not os.path.exists(pngDir):
    os.mkdir(pngDir)

frame_number=10
n_frames=frame_number
# n_frames=im.n_frames
width=im.width
height=im.height
print("source Image",width,height)
left = 0
right = 0


new_width=64
new_height=64

target = Image.new('RGB',(new_width*n_frames,new_height))#最终拼接的图像的大小
print(new_width,new_height,n_frames)
frame_i=0
try:
    while True:
        frame_i+=1
        current = im.tell()


        # b = im.resize((new_width, new_height), Image.ANTIALIAS)

        box = (width/4, height/4,  3*width/4-15, 3*height/4-40,)
        b = im.crop(box)
        b = b.resize((new_width, new_height), Image.ANTIALIAS)

        # b = b.rotate(10, )
        rect=(left,0,left+new_width,new_height)
        target.paste(b,rect,b.convert('RGBA'))

        left+=new_width
        im.seek(current + 1)
        if frame_i>frame_number:
            break

except EOFError:
    pass
target.save(pngDir + '/' + str(n_frames) + '.png', quality=100)
# im = Image.open(bath_path+filename)

# try:
#     while True:
#         # 保存当前帧图片
#         current = im.tell()
#         im.save(pngDir + '/' + str(current) + '.png')
#         # 获取下一帧图片
#         im.seek(current + 1)
# except EOFError:
#     pass

#
#

