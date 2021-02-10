from tkinter import *
from tkinter import ttk
import tkinter as tk
import pygame
import random
import os


class PygameTkinter():
    def __init__(self, view_port_size, map_editor):
        self.map_editor = map_editor
        self.tk_root = Tk()
        self.screen_frame = Frame(self.tk_root, width=view_port_size[0], height=view_port_size[1])
        self.screen_frame.grid(row=0, column=0)

        self.paint_frame = Frame(self.tk_root, width=640, height=480)
        self.paint_frame.grid(row=0, column=1)
        self.tk_sprite_tree = ttk.Treeview(self.paint_frame, show="tree")
        self.sprite_set()
        self.tk_sprite_tree.bind('<<TreeviewSelect>>', self.selectSprite)
        self.tk_sprite_tree.grid(row=1, column=0)

        self.tk_tile_tree = ttk.Treeview(self.paint_frame, show="tree")
        self.tile_set()
        self.tk_tile_tree.bind('<<TreeviewSelect>>', self.selectTile)
        self.tk_tile_tree.grid(row=2, column=0)

        self.playpausebutton = Button(self.paint_frame, command=self.playpause, text="Play/Pause")
        self.playpausebutton.grid(row=3, column=0)

        self.saveButton = Button(self.paint_frame, command=self.save_map, text="save map")
        self.saveButton.grid(row=3, column=1)

    def save_map(self):
        self.map_editor.write()

    def playpause(self):
        print(222)

    def selectTile(self, event):
        for item in self.tk_tile_tree.selection():
            item_text = self.tk_tile_tree.item(item, "values")
            print(item_text)
            self.map_editor.pen.tile_type = int(item_text[0])
            self.map_editor.pen.sprite_type = None

    def selectSprite(self, event):
        for item in self.tk_sprite_tree.selection():
            item_text = self.tk_sprite_tree.item(item, "values")
            print(item_text)
            self.map_editor.pen.sprite_type = int(item_text[0])
            self.map_editor.pen.tile_type = None

    def init_pygame(self):
        self.tk_root.update()
        os.environ['SDL_WINDOWID'] = str(self.screen_frame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

    def sprite_set(self):
        myid = self.tk_sprite_tree.insert("", 1, "tile1", text="企鹅", values=("1"))  # ""表示父节点是根
        myid = self.tk_sprite_tree.insert("", 2, "tile2", text="Ghost", values=("2"))  # ""表示父节点是根
        myid = self.tk_sprite_tree.insert("", 3, "tile3", text="Xiaohua", values=("3"))  # ""表示父节点是根
        myid = self.tk_sprite_tree.insert("", 4, "tile4", text="Phoenix", values=("4"))  # ""表示父节点是根

    def tile_set(self):
        # myid = self.tk_tile_tree.insert("", 0, "tile999", text="石地", values=("999"))  # ""表示父节点是根

        myid = self.tk_tile_tree.insert("", 0, "tile1", text="石地", values=("0"))  # ""表示父节点是根
        myid = self.tk_tile_tree.insert("", 1, "tile2", text="草", values=("1"))  # ""表示父节点是根
        myid = self.tk_tile_tree.insert("", 2, "tile3", text="石地2", values=("2"))  # ""表示父节点是根
        myid = self.tk_tile_tree.insert("", 3, "tile4", text="水", values=("3"))  # ""表示父节点是根
        # myidx1 = self.tk_tile_tree.insert(myid, 0, "广东", text="中国广东", values=("2"))  # text表示显示出的文本，values是隐藏的值

        # myidx1 = self.tile_tree.insert(myid, 0, "广东", text="中国广东", values=("2"))  # text表示显示出的文本，values是隐藏的值
        # myidx2 = self.tile_tree.insert(myid, 1, "江苏", text="中国江苏", values=("3"))
        # myidy = self.tile_tree.insert("", 1, "美国", text="美国USA", values=("4"))
        # myidy1 = self.tile_tree.insert(myidy, 0, "加州", text="美国加州", values=("5"))
