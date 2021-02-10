from tkinter import *
from tkinter import ttk
import tkinter as tk
import pygame
import random
import os
global playing
playing=False
def playpause():
    global playing
    if playing==True:
        playing=False
    else:
        playing=True
root = Tk()
screen_frame = Frame(root, width=640, height=480)
screen_frame.grid(row=0,column=0)



paint_frame= Frame(root,width=640, height=480)
paint_frame.grid(row=0,column=1)

sprite_tree = ttk.Treeview(paint_frame, show = "tree")
myid=sprite_tree.insert("",0,"中国",text="中国China",values=("1"))  # ""表示父节点是根
myidx1=sprite_tree.insert(myid,0,"广东",text="中国广东",values=("2"))  # text表示显示出的文本，values是隐藏的值
myidx2=sprite_tree.insert(myid,1,"江苏",text="中国江苏",values=("3"))
myidy=sprite_tree.insert("",1,"美国",text="美国USA",values=("4"))
myidy1=sprite_tree.insert(myidy,0,"加州",text="美国加州",values=("5"))
def selectTree(event):
    for item in sprite_tree.selection():
        item_text = sprite_tree.item(item, "values")
        print(item_text)
# 选中行
sprite_tree.bind('<<TreeviewSelect>>', selectTree)
# sprite_tree.pack(expand=True, fill=tk.BOTH)
sprite_tree.grid(row=0,column=0)

tile_tree = ttk.Treeview(paint_frame, show = "tree")
myid=tile_tree.insert("",0,"中国",text="中国China",values=("1"))  # ""表示父节点是根
myidx1=tile_tree.insert(myid,0,"广东",text="中国广东",values=("2"))  # text表示显示出的文本，values是隐藏的值
myidx2=tile_tree.insert(myid,1,"江苏",text="中国江苏",values=("3"))
myidy=tile_tree.insert("",1,"美国",text="美国USA",values=("4"))
myidy1=tile_tree.insert(myidy,0,"加州",text="美国加州",values=("5"))

def selectTree(event):
    for item in tile_tree.selection():
        item_text = tile_tree.item(item, "values")
        print(item_text)
# 选中行
tile_tree.bind('<<TreeviewSelect>>', selectTree)
# tile_tree.pack(expand=True, fill=tk.BOTH)
tile_tree.grid(row=1,column=0)


playpausebutton=Button(paint_frame, command=playpause, text="Play/Pause")
playpausebutton.grid(row=2,column=0)

# root.update()
os.environ['SDL_WINDOWID'] = str(screen_frame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
screen = pygame.display.set_mode((640,480))
# pygame.display.flip()
while True:
    #your code here
    if playing:
            screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.flip()
    root.update()