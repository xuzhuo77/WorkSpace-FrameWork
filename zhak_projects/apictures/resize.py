new_width=64*2
new_height=64*2

from PIL import Image
import os
bath_path='D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\tiles\\'
#
#
# for filename in ["tile1","tile2","tile3","tile4"]:
#     im = Image.open(bath_path+filename+".jpg")
#     target = im.resize((new_width, new_height), Image.ANTIALIAS)
#     target.save(bath_path + filename+ '.png', quality=100)

new_width=64
new_height=64
# for filename in ["sakula","sakula1","songshu1","songshu2"]:
#     im = Image.open("D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\"+filename+".jpg")
#     target = im.resize((new_width, new_height), Image.ANTIALIAS)
#     target.save(bath_path + filename+ '.png', quality=100)

# bath_path="E:\\pythonWebWorkSpace\\zhak_projects\\agame\\statics\\"
# bath_path='D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\'
#
#
# for filename in ["gun"]:
#     im = Image.open(bath_path+filename+".jpg")
#     im= im.transpose(Image.FLIP_LEFT_RIGHT)
#     target = im.resize((new_width, new_height), Image.ANTIALIAS)
#     target.save(bath_path + filename+ '.png', quality=100)
import time

output_path=os.getcwd()+os.sep+time.strftime("%Y%m%d%H%M%S", time.localtime())+os.sep

def rotate_images(image_filename_list,image_sizes):
    for filename,size in zip(image_filename_list,image_sizes):
        im = Image.open("D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\"+filename)
        target = im.resize((size[0], size[1]), Image.ANTIALIAS)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        if ".png" in filename:
            target.save(output_path + filename, quality=100)
        else:
            target.save(output_path + filename.split(".")[0]+".png", quality=100)
image_filename_list=["bullet.png"]
image_sizes=[(32,32)]
rotate_images(image_filename_list,image_sizes)

print(output_path )