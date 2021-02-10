
from PIL import Image
import os
bath_path='D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\'
# bath_path='E:\\pythonWebWorkSpace\\zhak_projects\\agame\\statics\\'
# filename="E:\\pythonWebWorkSpace\\zhak_projects\\apictures\\xiezi\\raw.png"
filename = bath_path+'explod2.gif'

n_frames=37
source_im = Image.open(filename)
print(source_im)
source_width=658
source_height=658

target_width=658
target_height=658

target = Image.new('RGBA',(target_width*n_frames,target_height))#最终拼接的图像的大小
print(target)
left=0
source_left=0
source_top=0
for i in range(n_frames):
    box = (source_left, 0, source_left+source_width, source_height)
    # box = (0, source_top, source_left, source_height+source_top)
    im= source_im.crop(box)
    source_left+=source_width
    # source_top+=source_height

    im=im.transpose(Image.FLIP_LEFT_RIGHT)
    b = im.resize((target_width, target_height), Image.ANTIALIAS)
    rect=(left,0,left+target_width,target_height)
    target.paste(b,rect,b.convert('RGBA'))
    left += target_width

target.save( str(n_frames) + '.png', quality=100)
