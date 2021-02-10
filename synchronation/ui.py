

# 导入tkinter模块

import tkinter
from tkinter import messagebox
import copy
from tkinter import *
import os

from synchronation.tableNameService import getColumnsFromSql

2
from tkinter import ttk

import sys


sys.path.append("..")
newTableColumns=[]


def upatetableColumns():
    for k,v in enumerate(newTableColumns):
        tree1.insert("",k,values=v)


def load_columns_from_table():
    base_path = E1.get()
    sql="select column_name from user_tab_columns   where Table_Name='{}'".format(base_path)
    result =getColumnsFromSql(sql)
    for k, v in enumerate(result):
        newTableColumns.append((v[0].strip('\''),))
    for k, v in enumerate(newTableColumns):
        tree1.insert("", k, values=v)


# 创建主窗口对象
root = tkinter.Tk()
# root.geometry("300x200+10+20")
root.minsize(1200, 500)

f1 = tkinter.Frame(root)
f11 = tkinter.Frame(f1)
f11.grid(row=0,column=0)

f1.grid(row=0, column=0)
l1 = Label(f11,text="新表名")
l1.grid(row=0, column=0)

E1 = Entry(f11, bd=1, )
E1.grid(row=1, column=0)
E1.insert(END, "Z_DOC")

l1 = Label(f11,text="新表列名")
l1.grid(row=2, column=0)
b1 = Button(f11, width=12, text='载入库', command=load_columns_from_table)
b1.grid(row=2, column=1)

tree1 = ttk.Treeview(f1)
tree1.grid(row=3, column=0)

tree1["columns"] = ("列名", "解释", )     # #定义列
tree1.column("#0",minwidth=0,width=100, stretch=NO)
tree1.column("列名", width=100)          # #设置列
tree1.column("解释", width=100)
tree1.heading("列名", text="列名")        # #设置显示的表头名
tree1.heading("解释", text="解释")

def treeviewClick(event):  # 单击
    for item in tree1.selection():
        item_text = tree1.item(item, "value")
        print(item_text)  # 输出所选行的第一列的值
        item_text=(8,8)
tree1.bind('<ButtonRelease-1>', treeviewClick)  # 绑定单击离开事件===========















# 加入消息循环
root.mainloop()
