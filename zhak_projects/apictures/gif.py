from PIL import Image

bath_path='D:\\WorkSpace-FrameWork\\zhak_projects\\agame\\statics\\'
im=Image.open(bath_path+'explod2.gif')
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")